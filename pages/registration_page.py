# pages/registration_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators from your script
        self.human_icon = (By.XPATH, "//div[@class='social-icon-cont']/div[1]")
        self.switch_to_signup_link = (By.XPATH, "//a[@class='switch-link']")
        self.fullname_input = (By.XPATH, "//input[@placeholder='Full Name']")
        self.email_input = (By.XPATH, "//input[@type='email']")
        self.password_input = (By.XPATH, "//input[@type='password']")
        self.submit_button = (By.XPATH, "//button[@type='submit']")

        # New success message locator matching your toast notification element class
        self.success_toast = (By.CLASS_NAME, "go3958317564")

    def navigate_to_signup(self):
        """Clicks the human icon and transitions the modal to the registration form."""
        icon = self.wait.until(EC.element_to_be_clickable(self.human_icon))
        icon.click()

        switch_link = self.wait.until(EC.element_to_be_clickable(self.switch_to_signup_link))
        switch_link.click()

    def register_user(self, name, email, password):
        """Fills out the registration form details and submits."""
        name_field = self.wait.until(EC.element_to_be_clickable(self.fullname_input))
        name_field.clear()
        name_field.send_keys(name)

        email_field = self.wait.until(EC.element_to_be_clickable(self.email_input))
        email_field.clear()
        email_field.send_keys(email)

        pass_field = self.wait.until(EC.element_to_be_clickable(self.password_input))
        pass_field.clear()
        pass_field.send_keys(password)

        btn = self.wait.until(EC.element_to_be_clickable(self.submit_button))
        btn.click()

    def get_success_message(self):
        """Extracts and returns the text from the registration success toast notification."""
        element = self.wait.until(EC.visibility_of_element_located(self.success_toast))
        return element.text