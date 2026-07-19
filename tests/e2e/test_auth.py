import uuid

from playwright.sync_api import Page, expect


BASE_URL = "http://127.0.0.1:8000"


def test_user_registration(page: Page):
    unique_value = uuid.uuid4().hex[:8]
    username = f"student_{unique_value}"
    email = f"student_{unique_value}@example.com"
    password = "Password123"

    page.goto(f"{BASE_URL}/register-page")

    page.fill("#username", username)
    page.fill("#email", email)
    page.fill("#password", password)
    page.fill("#confirm-password", password)

    page.click("button[type='submit']")

    expect(page.locator("#message")).to_have_text(
        "Registration successful."
    )

    access_token = page.evaluate(
        "localStorage.getItem('access_token')"
    )

    assert access_token is not None
    assert len(access_token) > 0


def test_user_login(page: Page):
    unique_value = uuid.uuid4().hex[:8]
    username = f"login_{unique_value}"
    email = f"login_{unique_value}@example.com"
    password = "Password123"

    page.goto(f"{BASE_URL}/register-page")

    page.fill("#username", username)
    page.fill("#email", email)
    page.fill("#password", password)
    page.fill("#confirm-password", password)

    page.click("button[type='submit']")

    expect(page.locator("#message")).to_have_text(
        "Registration successful."
    )

    page.goto(f"{BASE_URL}/login-page")

    page.fill("#email", email)
    page.fill("#password", password)

    page.click("button[type='submit']")

    expect(page.locator("#message")).to_have_text(
        "Login successful!"
    )

    access_token = page.evaluate(
        "localStorage.getItem('access_token')"
    )

    assert access_token is not None
    assert len(access_token) > 0


def test_password_mismatch_validation(page: Page):
    page.goto(f"{BASE_URL}/register-page")

    page.fill("#username", "teststudent")
    page.fill("#email", "teststudent@example.com")
    page.fill("#password", "Password123")
    page.fill("#confirm-password", "Different123")

    page.click("button[type='submit']")

    expect(page.locator("#message")).to_have_text(
        "Passwords do not match."
    )