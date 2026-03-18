import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_signup_and_login():
    # Signup
    response = client.post("/auth/signup", json={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert response.json()["msg"] == "User created"

    # Duplicate signup
    response_dup = client.post("/auth/signup", json={"username": "testuser", "password": "testpass"})
    assert response_dup.status_code == 400

    # Login
    response_login = client.post("/auth/login", json={"username": "testuser", "password": "testpass"})
    assert response_login.status_code == 200
    assert "access_token" in response_login.json()
