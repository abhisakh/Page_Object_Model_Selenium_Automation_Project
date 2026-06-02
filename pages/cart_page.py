# pages/cart_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # The shipping fee is the second h5 inside the shipment-container
        self.shipping_cost = (By.CSS_SELECTOR, ".shipment-container h5:last-child")
        self.product_total = (By.CSS_SELECTOR, ".product-total-container h5:last-child")
        self.cart_total = (By.CSS_SELECTOR, ".total-container h5:last-child")
        self.threshold_msg = (By.CLASS_NAME, "free-shipment-message")

        # Header Basket Tab Selector
        self.basket_tab = (By.XPATH, "//div[@class='social-icon-cont']/div[@class='headerIcon'][last()]")

        # Shipment Address Selectors
        self.street_input = (By.NAME, "street")
        self.city_input = (By.NAME, "city")
        self.postal_code_input = (By.NAME, "postalCode")

        # Payment Details Selectors
        self.card_number_input = (By.NAME, "cardNumber")
        self.card_name_input = (By.NAME, "nameOnCard")
        self.expiration_input = (By.NAME, "expiration")
        self.cvv_input = (By.NAME, "cvv")

        # Final Purchase Button
        self.buy_now_button = (By.CLASS_NAME, "btn-buy-now")

    def go_to_cart(self):
        """Clicks the dynamic basket icon tab."""
        self.wait.until(EC.element_to_be_clickable(self.basket_tab)).click()

    def get_shipping_fee(self):
        """Extracts numerical value from shipment field (e.g., '5€' -> 5.0)."""
        fee_text = self.wait.until(EC.visibility_of_element_located(self.shipping_cost)).text
        return float(fee_text.replace("€", "").strip())

    def get_product_total(self):
        """Returns the total price of products before shipping."""
        total_text = self.wait.until(EC.visibility_of_element_located(self.product_total)).text
        return float(total_text.replace("€", "").strip())

    def get_threshold_message(self):
        """Returns the free shipping hint text."""
        return self.wait.until(EC.visibility_of_element_located(self.threshold_msg)).text

    # def complete_checkout(self, street, city, postal_code, card_num, card_name, expiry, cvv):
    #     """Fills out the shipment and payment form, then clicks Buy Now."""
    #     self.wait.until(EC.visibility_of_element_located(self.street_input)).send_keys(street)
    #     self.driver.find_element(*self.city_input).send_keys(city)
    #     self.driver.find_element(*self.postal_code_input).send_keys(postal_code)

    #     self.driver.find_element(*self.card_number_input).send_keys(card_num)
    #     self.driver.find_element(*self.card_name_input).send_keys(card_name)
    #     self.driver.find_element(*self.expiration_input).send_keys(expiry)
    #     self.driver.find_element(*self.cvv_input).send_keys(cvv)

    #     self.wait.until(EC.element_to_be_clickable(self.buy_now_button)).click()

    def complete_checkout(self, street, city, postal_code, card_num, card_name, expiry, cvv):
        """Fills out the checkout form with strict explicit waits on all elements."""
        fields = [
            (self.street_input, street),
            (self.city_input, city),
            (self.postal_code_input, postal_code),
            (self.card_number_input, card_num),
            (self.card_name_input, card_name),
            (self.expiration_input, expiry),
            (self.cvv_input, cvv)
        ]

        for locator, value in fields:
            self.wait.until(EC.element_to_be_clickable(locator)).send_keys(value)

        self.wait.until(EC.element_to_be_clickable(self.buy_now_button)).click()

    def clear_entire_cart(self):
        """Repeatedly removes the first product card until the cart container is completely empty."""
        while True:
            try:
                # Look for any remaining remove icons with a very short timeout
                remove_buttons = self.driver.find_elements(By.CLASS_NAME, "remove-icon")
                if not remove_buttons:
                    break

                # Always click the first one available, then wait for the DOM to settle
                remove_buttons[0].click()
                WebDriverWait(self.driver, 2).until(
                    EC.staleness_of(remove_buttons[0])
                )
            except:
                break