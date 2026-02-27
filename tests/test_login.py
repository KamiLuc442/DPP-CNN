import pytest
from fastapi.testclient import TestClient
from src.auth.crud import create_user


def test_login_success(client: TestClient, db_session):
    create_user(db_session, "testuser", "password123", ["ROLE_USER"])
    
    response = client.post(
        "/auth/login",
        json={"login": "testuser", "password": "password123"}
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    assert data["user"]["login"] == "testuser"
    assert "ROLE_USER" in data["user"]["roles"]


def test_login_wrong_password(client: TestClient, db_session):
    create_user(db_session, "testuser2", "correctpassword", ["ROLE_USER"])
    
    response = client.post(
        "/auth/login",
        json={"login": "testuser2", "password": "wrongpassword"}
    )
    
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect login or password"


def test_login_nonexistent_user(client: TestClient, db_session):
    response = client.post(
        "/auth/login",
        json={"login": "nonexistent", "password": "password123"}
    )
    
    assert response.status_code == 401
    assert response.json()["detail"] == "Incorrect login or password"


def test_login_missing_fields(client: TestClient, db_session):
    response = client.post(
        "/auth/login",
        json={"login": "testuser"}
    )
    
    assert response.status_code == 422


def test_login_empty_credentials(client: TestClient, db_session):
    response = client.post(
        "/auth/login",
        json={"login": "", "password": ""}
    )
    
    assert response.status_code == 401
