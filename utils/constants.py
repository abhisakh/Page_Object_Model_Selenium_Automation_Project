# utils/constants.py

# utils/constants.py

BASE_URL = "https://grocerymate.masterschool.com"
STORE_URL = f"{BASE_URL}/store"

# Test Account Credentials
USER_EMAIL = "abhisakh_3@gmail.com"
USER_PASS = "Falguni1982"

# Expected Error Messages
ERR_MAX_REVIEW = "Feedback cannot exceed 500 characters."
ERR_EMPTY_REVIEW = "Error message displayed"  # Adjust based on site UI behavior

ALCOHOL_CAT_URL = f"{BASE_URL}/category/alcohol"

# Shipping Thresholds
SHIPPING_THRESHOLD = 20.00
STANDARD_SHIPPING_FEE = 5.00

# Error Messages
ERR_AGE_DENIED = "You are underage. You can still browse the site, but you will not be able to view alcohol products."
ERR_MAX_CHAR = "Feedback cannot exceed 500 characters."