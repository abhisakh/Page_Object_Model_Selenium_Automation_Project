# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.email_input = (By.CSS_SELECTOR, "input[type='email']")
        self.password_input = (By.CSS_SELECTOR, "input[type='password']")
        self.submit_button = (By.CSS_SELECTOR, "button[type='submit']")

    def login(self, email, password):
        email_field = self.wait.until(EC.element_to_be_clickable(self.email_input))
        email_field.clear()
        email_field.send_keys(email)

        pass_field = self.wait.until(EC.element_to_be_clickable(self.password_input))
        pass_field.clear()
        pass_field.send_keys(password)

        self.wait.until(EC.element_to_be_clickable(self.submit_button)).click()
        # Wait for the login URL to change, ensuring the session token loads
        self.wait.until(EC.url_changes(f"{self.driver.current_url}"))