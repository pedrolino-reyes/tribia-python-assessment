import os
import pytest

def test_login(page):
    login_user = os.getenv("LOGIN_USER", "")
    login_pass = os.getenv("LOGIN_PASS", "")

    if not login_user or not login_pass:
        raise Exception("Environment variables LOGIN_USER and LOGIN_PASS must be set")

    page.goto("/login")
    page.get_by_label("Username").fill(login_user)
    page.get_by_label("Password").fill(login_pass)
    page.get_by_role("button", name="Login").click()

    # Wait for the secure page to load.
    page.wait_for_url("/secure")

    assert "/secure" in page.url
    assert page.is_visible("text=You logged into a secure area!") is True
    h2_text = page.text_content("h2")
    assert h2_text is not None and "Secure Area" in h2_text
