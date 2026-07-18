from app.models import User
from tests.conftest import TestingSessionLocal


def test_register_user(client):
    response = client.post(
        "/users/register",
        json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["username"] == "testuser"
    assert data["email"] == "testuser@example.com"
    assert "id" in data
    assert "created_at" in data
    assert "password" not in data
    assert "password_hash" not in data

    with TestingSessionLocal() as db:
        saved_user = (
            db.query(User)
            .filter(User.username == "testuser")
            .first()
        )

        assert saved_user is not None
        assert saved_user.email == "testuser@example.com"
        assert saved_user.password_hash != "password123"


def test_register_duplicate_username(client):
    user_data = {
        "username": "duplicateuser",
        "email": "first@example.com",
        "password": "password123",
    }

    first_response = client.post(
        "/users/register",
        json=user_data,
    )

    second_response = client.post(
        "/users/register",
        json={
            "username": "duplicateuser",
            "email": "second@example.com",
            "password": "password123",
        },
    )

    assert first_response.status_code == 201
    assert second_response.status_code == 400
    assert second_response.json()["detail"] == "Username already exists."


def test_register_duplicate_email(client):
    first_response = client.post(
        "/users/register",
        json={
            "username": "firstuser",
            "email": "duplicate@example.com",
            "password": "password123",
        },
    )

    second_response = client.post(
        "/users/register",
        json={
            "username": "seconduser",
            "email": "duplicate@example.com",
            "password": "password123",
        },
    )

    assert first_response.status_code == 201
    assert second_response.status_code == 400
    assert second_response.json()["detail"] == "Email already exists."


def test_login_user_successfully(client):
    client.post(
        "/users/register",
        json={
            "username": "loginuser",
            "email": "loginuser@example.com",
            "password": "password123",
        },
    )

    response = client.post(
        "/users/login",
        json={
            "username": "loginuser",
            "password": "password123",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Login successful."
    assert data["username"] == "loginuser"
    assert "user_id" in data


def test_login_with_wrong_password(client):
    client.post(
        "/users/register",
        json={
            "username": "wrongpassworduser",
            "email": "wrongpassword@example.com",
            "password": "password123",
        },
    )

    response = client.post(
        "/users/login",
        json={
            "username": "wrongpassworduser",
            "password": "incorrect123",
        },
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid username or password."


def test_login_nonexistent_user(client):
    response = client.post(
        "/users/login",
        json={
            "username": "missinguser",
            "password": "password123",
        },
    )

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid username or password."