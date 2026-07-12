from app.security import hash_password, verify_password


def test_hash_password():
    password = "password123"

    hashed_password = hash_password(password)

    assert hashed_password != password
    assert isinstance(hashed_password, str)


def test_verify_correct_password():
    password = "password123"
    hashed_password = hash_password(password)

    assert verify_password(password, hashed_password) is True


def test_verify_incorrect_password():
    hashed_password = hash_password("password123")

    assert verify_password("wrongpassword", hashed_password) is False