# tests/test_registration.py
from pages.registration_page import RegistrationPage
from utils import constants

def test_user_registration_flow(driver, random_user_credentials):
    """Verifies that a new user registration workflow submits correctly."""
    driver.get(f"{constants.BASE_URL}")

    name = random_user_credentials["name"]
    email = random_user_credentials["email"]
    password = random_user_credentials["password"]

    registration_page = RegistrationPage(driver)
    registration_page.navigate_to_signup()
    registration_page.register_user(name, email, password)

    # Validate that the registration confirmation status appears
    actual_msg = registration_page.get_success_message()
    expected_msg = "Registration successful. Please log in."

    assert actual_msg == expected_msg, f"Expected alert '{expected_msg}' but got '{actual_msg}'"