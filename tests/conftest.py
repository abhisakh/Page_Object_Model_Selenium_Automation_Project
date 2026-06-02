# tests/conftest.py
import os
import uuid
import pytest
from selenium import webdriver

@pytest.fixture
def random_user_credentials():
    """Generates unique user data fresh for each test execution."""
    unique_id = uuid.uuid4().hex[:8]
    return {
        "name": f"Automation_User_{unique_id}",
        "email": f"tester_{unique_id}@example.com",
        "password": "SecurePass123!"
    }

@pytest.fixture(scope="function")
def driver(request):
    """Initializes and tears down the Selenium WebDriver instance."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    # Initialize driver
    driver = webdriver.Chrome(options=options)

    # Provide the driver instance to the test class/function
    yield driver

    # Fail-safe screenshot capture on test failure
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshot_dir = os.path.join(os.path.dirname(__file__), "..", "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{request.node.name}.png")
        driver.save_screenshot(screenshot_path)

    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Pytest hook to attach test execution status to the request node."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)