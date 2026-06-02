# tests/test_shipping.py
import pytest
import time
from pages.login_page import LoginPage
from pages.age_verification_page import AgeVerificationPage
from pages.store_page import StorePage
from pages.cart_page import CartPage
from utils import constants
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_and_clear_stale_cart(driver):
    """Prerequisite: Authenticates and ensures the cart is 100% empty."""
    print(f"\n[PREREQUISITE] Authenticating user: {constants.USER_EMAIL}")
    driver.get(f"{constants.BASE_URL}/auth")
    LoginPage(driver).login(constants.USER_EMAIL, constants.USER_PASS)

    print("[PREREQUISITE] Handling age gate check...")
    age_page = AgeVerificationPage(driver)
    age_page.navigate_to_store()
    if age_page.is_modal_visible():
        age_page.enter_dob("01-01-2000")

    print("[PREREQUISITE] Navigating to cart to clear stale items...")
    cart_page = CartPage(driver)
    cart_page.go_to_cart()
    try:
        cart_page.clear_entire_cart()
        print("[PREREQUISITE] Cart cleared successfully.")
    except:
        print("[PREREQUISITE] Cart was already empty.")

@pytest.mark.parametrize("quantity, expected_shipping", [
    (28, 5.00),  # 28 * 0.70€ = 19.60€ (Below 20€ threshold -> 5€ shipping)
    (29, 0.00),  # 29 * 0.70€ = 20.30€ (Above 20€ threshold -> 0€ shipping)
])
def test_shipping_costs_bva(driver, quantity, expected_shipping):
    # 1. Clean cart state before running test calculations
    login_and_clear_stale_cart(driver)

    print(f"\n==========================================")
    print(f"[START] BVA Loop: Qty {quantity} | Target Shipping: {expected_shipping}€")
    print(f"==========================================")

    # 2. Return to store grid and add items sequentially using working flow
    print(f"[STEP 1] Adding {quantity} items of 'Celery' from store grid...")
    store_page = StorePage(driver)
    driver.get(f"{constants.BASE_URL}/store")
    for _ in range(quantity):
        store_page.add_product_to_cart("Celery")

    # 3. Navigate back to checkout validation container
    print("[STEP 2] Navigating to cart page to calculate totals...")
    cart_page = CartPage(driver)
    cart_page.go_to_cart()

    actual_product_total = cart_page.get_product_total()
    actual_shipping = cart_page.get_shipping_fee()

    print(f"[STEP 3] Calculation results -> Product Total: {actual_product_total}€ | Shipping Fee: {actual_shipping}€")

    assert actual_shipping == expected_shipping, (
        f"For product total of {actual_product_total}€, "
        f"expected {expected_shipping}€ shipping but received {actual_shipping}€."
    )
    print(f"[PASS] BVA check for {quantity} units completed successfully.")
    print("[PREREQUISITE] Navigating to cart to clear stale items...")
    cart_page = CartPage(driver)
    cart_page.go_to_cart()
    try:
        cart_page.clear_entire_cart()
        print("[PREREQUISITE] Cart cleared successfully.")
    except:
        print("[PREREQUISITE] Cart was already empty.")


def test_shipping_cost_empty_cart(driver):
    """Test Case 9: Empty cart scenario - verifies no shipping component is displayed."""
    wait = WebDriverWait(driver, 10)

    # 1. Clear cart state before running test calculations
    login_and_clear_stale_cart(driver)

    print(f"\n==========================================")
    print(f"[START] Error Guessing Test: Empty Cart View State")
    print(f"==========================================")

    # 2. Directly verify the empty cart container replaces checkout summary details
    print("[STEP 1] Checking layout tree for empty container selector...")
    empty_container = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "empty-cart-container"))
    )

    # 3. Assert header elements exist and summary panels are absent
    print("[STEP 2] Verifying 'Your cart is empty' header layout matches...")
    empty_header = empty_container.find_element(By.TAG_NAME, "h2").text
    assert empty_header == "Your cart is empty", f"Unexpected empty view header text: '{empty_header}'"

    print("[STEP 3] Confirming price and shipping fee components are hidden from view...")
    shipping_elements = driver.find_elements(By.ID, "shipping-fee")
    assert len(shipping_elements) == 0, "Found shipping fee calculation element on an empty cart layout view!"

    print(f"[PASS] Empty cart container validated. Shipping layout hidden safely.")

def test_shipping_fee_reduction_calculation_bug_003(driver):
    """
    BUG TRACKING - ID: BUG-003
    Description: Verifies that shipping cost remains stuck at 0€ even when
    the total drops below 20€ due to a reduction in item quantities.
    """
    wait = WebDriverWait(driver, 10)

    # 1. Clean cart state before running test calculations
    login_and_clear_stale_cart(driver)

    print(f"\n==========================================")
    print(f"[START] BUG-003: Shipping Fee Reduction Regression")
    print(f"==========================================")

    # 2. Add 30 items to push the total well above 20€ threshold (Free Shipping)
    print("[STEP 1] Adding 30 units of Celery to cross the 20€ free shipping barrier...")
    store_page = StorePage(driver)
    driver.get(f"{constants.BASE_URL}/store")
    for _ in range(30):
        store_page.add_product_to_cart("Celery")

    # 3. Navigate to checkout and confirm free shipping is active
    print("[STEP 2] Moving to checkout container to verify initial 0€ state...")
    cart_page = CartPage(driver)
    cart_page.go_to_cart()

    initial_total = cart_page.get_product_total()
    initial_shipping = cart_page.get_shipping_fee()
    print(f"[STEP 2.1] Current total: {initial_total}€ | Shipping fee is: {initial_shipping}€")
    assert initial_shipping == 0.00, "Setup failed: Initial shipping should be free."

    # 4. Use the item removal functionality to drop below the threshold
    print("[STEP 3] Decreasing item count below threshold (removing 29 items)...")
    remove_btn_xpath = "//button[contains(@class, 'remove-single-item') or text()='-']"

    # Loop to click minus button 29 times safely
    for i in range(29):
        minus_button = wait.until(EC.element_to_be_clickable((By.XPATH, remove_btn_xpath)))
        minus_button.click()

        try:
            wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading-spinner")))
        except:
            pass
        time.sleep(0.3)

    print("[STEP 3.1] Reductions complete. Waiting 2s for layout synchronization...")
    time.sleep(2)

    # 5. Extract values from shipment-container layout structure
    print("[STEP 4] Locating shipment container text nodes...")
    shipment_card = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shipment-container"))
    )

    shipping_value_text = shipment_card.find_elements(By.TAG_NAME, "h5")[1].text
    print(f"[STEP 4.1] Extracted DOM shipping fee value text displays: '{shipping_value_text}'")

    # 6. Assert bug behavior to ensure test returns a green SUCCESS state
    new_total = cart_page.get_product_total()
    print(f"[STEP 5] Final Calculation -> New Product Total: {new_total}€ | Shipping Expected by Bug: 0€")

    numeric_shipping = "".join(filter(str.isdigit, shipping_value_text))

    # Expect '0' to confirm the bug is actively present on the site
    assert numeric_shipping == "0", (
        f"BUG RESOLVED: Shipping updated dynamically or changed from 0€ to {shipping_value_text}."
    )
    print(f"[PASS] BUG-003 VERIFIED: Shipping cost incorrectly stayed stuck at '0€' for a total of {new_total}€.")