def test_create_user(client):
    response = client.post(
        "/users",
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
    assert "password" not in data
    assert "password_hash" not in data
    assert "id" in data
    assert "created_at" in data


def test_duplicate_username(client):
    first_user = {
        "username": "sameuser",
        "email": "first@example.com",
        "password": "password123",
    }

    second_user = {
        "username": "sameuser",
        "email": "second@example.com",
        "password": "password123",
    }

    first_response = client.post("/users", json=first_user)
    second_response = client.post("/users", json=second_user)

    assert first_response.status_code == 201
    assert second_response.status_code == 400
    assert second_response.json()["detail"] == "Username already exists."


def test_duplicate_email(client):
    first_user = {
        "username": "firstuser",
        "email": "same@example.com",
        "password": "password123",
    }

    second_user = {
        "username": "seconduser",
        "email": "same@example.com",
        "password": "password123",
    }

    first_response = client.post("/users", json=first_user)
    second_response = client.post("/users", json=second_user)

    assert first_response.status_code == 201
    assert second_response.status_code == 400
    assert second_response.json()["detail"] == "Email already exists."


def test_invalid_email(client):
    response = client.post(
        "/users",
        json={
            "username": "testuser",
            "email": "invalid-email",
            "password": "password123",
        },
    )

    assert response.status_code == 422


def test_short_password(client):
    response = client.post(
        "/users",
        json={
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "short",
        },
    )

    assert response.status_code == 422