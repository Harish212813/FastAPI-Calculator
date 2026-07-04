# tests/test_e2e.py

from playwright.sync_api import Page


def test_homepage(page: Page):
    page.goto("http://127.0.0.1:8000")
    assert "FastAPI Calculator is running" in page.text_content("body")


def test_add_endpoint_in_browser(page: Page):
    page.goto("http://127.0.0.1:8000/add?a=2&b=3")
    assert "5" in page.text_content("body")