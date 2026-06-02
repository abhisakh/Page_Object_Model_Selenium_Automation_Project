# tests/test_login.py
import pytest
import time
from pages.login_page import LoginPage
from utils import constants

def test_successful_login(driver):
    """Verifies that a user can successfully log in with valid credentials."""
    driver.get(f"{constants.BASE_URL}/auth")

    login_page = LoginPage(driver)
    login_page.login(constants.USER_EMAIL, constants.USER_PASS)

    time.sleep(2)
    # Validate successful navigation to the store after a login session
    assert driver.current_url == f"{constants.BASE_URL}/", f"Expected URL to be {constants.BASE_URL} but got {driver.current_url}"