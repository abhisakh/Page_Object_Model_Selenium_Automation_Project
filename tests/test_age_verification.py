import pytest
import time
from datetime import datetime, timedelta
from pages.login_page import LoginPage
from pages.age_verification_page import AgeVerificationPage
from utils import constants

# Dynamically calculate exact boundary dates based on today's date (2026)
today = datetime.now()
exact_18 = (today - timedelta(days=365 * 18 + 4)).strftime("%d-%m-%Y") # Account for leap years
underage_18 = (today - timedelta(days=365 * 18 - 1)).strftime("%d-%m-%Y")
adult_25 = (today - timedelta(days=365 * 25)).strftime("%d-%m-%Y")
child_14 = (today - timedelta(days=365 * 14)).strftime("%d-%m-%Y")

@pytest.mark.parametrize("dob, should_pass, expected_error", [
    (exact_18, True, None),
    (underage_18, False, constants.ERR_AGE_DENIED),
    (adult_25, True, None),
    (child_14, False, constants.ERR_AGE_DENIED),
    ("", False, constants.ERR_AGE_DENIED),          # Test Case 6: Empty Input [refer to my STLC/test_case_design.md]
    ("32-13-2020", False, constants.ERR_AGE_DENIED) # Test Case 7: Invalid Format [refer to my STLC/test_case_design.md]
])
def test_age_verification_boundaries(driver, dob, should_pass, expected_error):
    driver.get(f"{constants.BASE_URL}/auth")

    login_page = LoginPage(driver)
    login_page.login(constants.USER_EMAIL, constants.USER_PASS)

    age_page = AgeVerificationPage(driver)
    age_page.navigate_to_store()

    assert age_page.is_modal_visible(), "Age input field not displayed."

    # enter_dob handles empty strings safely as clear() is called first
    age_page.enter_dob(dob)
    #time.sleep(2) #. <---------------------------------------------------- For my own use

    if should_pass:
        assert not age_page.is_modal_visible(), "Modal remained visible for a valid adult profile."
    else:
        assert age_page.get_error_message() == expected_error