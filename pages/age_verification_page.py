# pages/age_verification_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AgeVerificationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # New navigational selector added to the POM mapping
        self.store_link = (By.CSS_SELECTOR, "a[href='/store']")
        self.dob_input = (By.CSS_SELECTOR, "input[placeholder='DD-MM-YYYY']")
        self.submit_btn = (By.CSS_SELECTOR, "button")
        self.error_msg = (By.XPATH, "//div[@role='status'][contains(text(), 'You are underage')]")

    def navigate_to_store(self):
        self.wait.until(EC.element_to_be_clickable(self.store_link)).click()

    def is_modal_visible(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.dob_input)).is_displayed()
        except:
            return False

    def enter_dob(self, dob_string):
        input_field = self.wait.until(EC.element_to_be_clickable(self.dob_input))
        input_field.clear()
        input_field.send_keys(dob_string)
        self.wait.until(EC.element_to_be_clickable(self.submit_btn)).click()

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.error_msg)).text