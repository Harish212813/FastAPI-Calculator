import pytest
from pydantic import ValidationError

from app.schemas import UserCreate


def test_valid_user_schema():
    user = UserCreate(
        username="akhil123",
        email="akhil@example.com",
        password="password123",
    )

    assert user.username == "akhil123"
    assert user.email == "akhil@example.com"
    assert user.password == "password123"


def test_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(
            username="akhil123",
            email="not-an-email",
            password="password123",
        )


def test_short_username():
    with pytest.raises(ValidationError):
        UserCreate(
            username="ab",
            email="akhil@example.com",
            password="password123",
        )


def test_short_password():
    with pytest.raises(ValidationError):
        UserCreate(
            username="akhil123",
            email="akhil@example.com",
            password="short",
        )