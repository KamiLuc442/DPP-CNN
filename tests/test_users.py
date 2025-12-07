import pytest
from fastapi.testclient import TestClient
from src.auth.crud import create_user
from src.auth.utils import get_password_hash


def create_admin(db_session, login="admin", password="admin123"):
    return create_user(
        db_session,
        login=login,
        password=password,
        roles=["ROLE_ADMIN"]
    )


def get_auth_header_for_user(client: TestClient, login: str, password: str):
    response = client.post("/auth/login", json={"login": login, "password": password})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_create_user_as_admin(client: TestClient, db_session):
    admin_user = create_admin(db_session)
    headers = get_auth_header_for_user(client, "admin", "admin123")

    response = client.post(
        "/users",
        json={"login": "newuser", "password": "newpass123", "roles": ["ROLE_USER"]},
        headers=headers
    )

    assert response.status_code == 201
    data = response.json()
    assert data["login"] == "newuser"
    assert "ROLE_USER" in data["roles"]


def test_create_user_without_admin(client: TestClient, db_session):
    create_user(db_session, "normaluser", "password123", ["ROLE_USER"])
    headers = get_auth_header_for_user(client, "normaluser", "password123")

    response = client.post(
        "/users",
        json={"login": "anotheruser", "password": "anotherpass"},
        headers=headers
    )

    assert response.status_code == 403
    assert "detail" in response.json()


def test_create_user_with_existing_login(client: TestClient, db_session):
    admin_user = create_admin(db_session)
    headers = get_auth_header_for_user(client, "admin", "admin123")

    create_user(db_session, "existinguser", "pass123", ["ROLE_USER"])

    response = client.post(
        "/users",
        json={"login": "existinguser", "password": "newpass123"},
        headers=headers
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Login already registered"


def test_create_user_missing_fields(client: TestClient, db_session):
    admin_user = create_admin(db_session)
    headers = get_auth_header_for_user(client, "admin", "admin123")

    response = client.post(
        "/users",
        json={"login": "userwithoutpassword"},
        headers=headers
    )

    assert response.status_code == 422
