import pytest
from fastapi.testclient import TestClient
from src.auth.crud import create_user


def get_auth_header_for_user(client: TestClient, login: str, password: str):
    response = client.post("/auth/login", json={"login": login, "password": password})
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_user_details_authorized(client: TestClient, db_session):
    create_user(db_session, "testuser", "password123", ["ROLE_USER"])
    
    headers = get_auth_header_for_user(client, "testuser", "password123")
    
    response = client.get("/auth/user_details", headers=headers)
    
    assert response.status_code == 200
    data = response.json()
    assert data["login"] == "testuser"
    assert "ROLE_USER" in data["roles"]
    assert "id" in data


def test_user_details_no_token(client: TestClient, db_session):
    response = client.get("/auth/user_details")
    
    assert response.status_code == 401
    assert "detail" in response.json()
