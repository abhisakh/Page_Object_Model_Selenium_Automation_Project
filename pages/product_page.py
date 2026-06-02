# pages/product_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Restriction Elements
        self.restriction_msg = (By.CSS_SELECTOR, ".reviewRestriction p")

        # Active Form Triggers & Elements
        self.add_comment_button = (By.XPATH, "//button[contains(text(), 'Add a comment')]")
        self.text_area = (By.CLASS_NAME, "new-review-form-control")
        self.stars = (By.CSS_SELECTOR, ".interactive-rating .star")
        self.char_counter = (By.CSS_SELECTOR, ".new-review-char-counter span")
        self.send_button = (By.CLASS_NAME, "new-review-btn-send")

    def get_restriction_message(self):
        """Returns restriction text if visible, or None if the form is available."""
        try:
            element = WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.restriction_msg)
            )
            return element.text
        except:
            return None

    def open_review_form(self):
        """Clicks the initial 'Add a comment' trigger button to expand the form."""
        try:
            btn = self.wait.until(EC.element_to_be_clickable(self.add_comment_button))
            btn.click()
            print("[DEBUG] 'Add a comment' button clicked.")
        except Exception as e:
            print(f"[DEBUG] Could not click 'Add a comment' button: {e}")

    def is_form_available(self):
        """Returns True if the form text area control element is visible."""
        try:
            return WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located(self.text_area)
            ).is_displayed()
        except:
            return False

    def select_rating(self, rating):
        """Clicks the star element matching the 1-5 scalar value."""
        all_stars = self.wait.until(EC.presence_of_all_elements_located(self.stars))
        all_stars[rating - 1].click()

    def enter_review_text(self, text):
        """Clears and fills input textarea field."""
        field = self.wait.until(EC.element_to_be_clickable(self.text_area))
        field.clear()
        field.send_keys(text)

    def get_counter_value(self):
        """Returns the current character counter text string."""
        return self.wait.until(EC.visibility_of_element_located(self.char_counter)).text

    def click_send(self):
        """Submits the current review form payload."""
        self.wait.until(EC.element_to_be_clickable(self.send_button)).click()