# # pages/store_page.py
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException

# class StorePage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)

#     # def select_product_by_name(self, product_name):
#     #     """Locates a product card by its name and clicks it to open details."""
#     #     # Using the 'lead' class from HTML snippet to find the specific product
#     #     product_xpath = f"//p[@class='lead' and contains(text(), '{product_name}')]"
#     #     self.wait.until(EC.element_to_be_clickable((By.XPATH, product_xpath))).click()

#     def select_product_by_name(self, product_name):
#         """
#         Scans the current shop page for the target product by its lead text class.
#         If not found, clicks the 'Next' pagination button and repeats until found.
#         """
#         print("[SHOP] Waiting for store page product layout grid to load...")
#         self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-card")))

#         while True:
#             print(f"[SHOP] Scanning current page for product: '{product_name}'...")
#             product_xpath = f"//p[@class='lead' and contains(text(), '{product_name}')]"
#             product_elements = self.driver.find_elements(By.XPATH, product_xpath)

#             if len(product_elements) > 0 and product_elements[0].is_displayed():
#                 print(f"[SUCCESS] Target product '{product_name}' located on this page!")
#                 # Click the element to open details as originally intended
#                 self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product_elements[0])
#                 time.sleep(0.5)
#                 product_elements[0].click()
#                 return

#             # Product not found, look for 'Next' pagination button
#             print(f"[INFO] '{product_name}' not on this page. Checking pagination...")
#             next_btn_xpath = "//li[contains(@class, 'pagination-item')]//button[text()='Next']"
#             next_buttons = self.driver.find_elements(By.XPATH, next_btn_xpath)

#             if not next_buttons:
#                 print("[ERROR] 'Next' pagination button could not be found in the DOM.")
#                 break

#             next_button = next_buttons[0]

#             # Check if the 'Next' button parent item layout is disabled or if the button itself is disabled
#             parent_li = next_button.find_element(By.XPATH, "./..")
#             is_disabled = "disabled" in parent_li.get_attribute("class") or not next_button.is_enabled()

#             if is_disabled:
#                 print("[END] Reached the final page. Target product was not found anywhere.")
#                 break

#             # Go to next page and synchronize stability states
#             print("[SHOP] Clicking 'Next' button to advance pagination...")
#             self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_button)
#             time.sleep(0.5)
#             next_button.click()

#             # Wait for page layout switch synchronization
#             time.sleep(2)
#             self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-card")))

#         raise NoSuchElementException(f"Could not locate product '{product_name}' across pagination pages.")

#     # def add_product_to_cart(self, product_name):
#     #     """Finds the 'Add to Cart' button for a specific product card."""
#     #     xpath = f"//div[@class='product-card' and .//p[text()='{product_name}']]//button[contains(text(), 'Add to Cart')]"
#     #     self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

#     def add_product_to_cart(self, product_name):
#         """Finds the 'Add to Cart' button for a specific product card using its unique class."""
#         xpath = f"//div[@class='product-card' and .//p[contains(text(), '{product_name}')]]//button[contains(@class, 'btn-cart')]"
#         self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

class StorePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_product_by_name(self, product_name):
        """
        Scans the current shop page for the target product by its lead text class.
        If not found, clicks the 'Next' pagination button and repeats until found.
        """
        print("[SHOP] Waiting for store page product layout grid to load...")
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-card")))

        while True:
            print(f"[SHOP] Scanning current page for product: '{product_name}'...")
            product_xpath = f"//p[@class='lead' and contains(text(), '{product_name}')]"
            product_elements = self.driver.find_elements(By.XPATH, product_xpath)

            if len(product_elements) > 0 and product_elements[0].is_displayed():
                print(f"[SUCCESS] Target product '{product_name}' located on this page!")
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product_elements[0])
                time.sleep(0.5)
                product_elements[0].click()
                return

            # Use helper to handle pagination flipping
            if not self._navigate_to_next_page(product_name):
                break

        raise NoSuchElementException(f"Could not locate product '{product_name}' across pagination pages.")

    def add_product_to_cart(self, product_name):
        """
        Scans pages for the specific product card using its unique class
        and clicks 'Add to Cart'. Flips pages if the product is not on the current page.
        """
        print("[SHOP] Waiting for store page product layout grid to load...")
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-card")))

        while True:
            print(f"[SHOP] Scanning current page to add product to cart: '{product_name}'...")
            xpath = f"//div[@class='product-card' and .//p[contains(text(), '{product_name}')]]//button[contains(@class, 'btn-cart')]"
            cart_buttons = self.driver.find_elements(By.XPATH, xpath)

            if len(cart_buttons) > 0 and cart_buttons[0].is_displayed():
                print(f"[SUCCESS] Target cart button for '{product_name}' located!")
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", cart_buttons[0])
                time.sleep(0.5)
                cart_buttons[0].click()
                return

            # Use helper to handle pagination flipping
            if not self._navigate_to_next_page(product_name):
                break

        raise NoSuchElementException(f"Could not locate cart button for '{product_name}' across pagination pages.")

    def _navigate_to_next_page(self, product_name):
        """
        Helper method to locate, validate, and click the 'Next' pagination button.
        Returns True if navigation succeeded, False if blocked or on the last page.
        """
        print(f"[INFO] '{product_name}' not on this page. Checking pagination...")
        next_btn_xpath = "//li[contains(@class, 'pagination-item')]//button[text()='Next']"
        next_buttons = self.driver.find_elements(By.XPATH, next_btn_xpath)

        if not next_buttons:
            print("[ERROR] 'Next' pagination button could not be found in the DOM.")
            return False

        next_button = next_buttons[0]

        # Check if the 'Next' button parent item layout is disabled or if the button itself is disabled
        parent_li = next_button.find_element(By.XPATH, "./..")
        is_disabled = "disabled" in parent_li.get_attribute("class") or not next_button.is_enabled()

        if is_disabled:
            print("[END] Reached the final page. Target item was not found anywhere.")
            return False

        # Go to next page and synchronize stability states
        print("[SHOP] Clicking 'Next' button to advance pagination...")
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_button)
        time.sleep(0.5)
        next_button.click()

        # Wait for page layout switch synchronization
        time.sleep(2)
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-card")))
        return True