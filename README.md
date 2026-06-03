# 🍎 GroceryMate QA Automation Framework (Page Object Model)

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.44.0-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-9.0.3-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-abhisakh-181717?style=for-the-badge&logo=github)](https://github.com/abhisakh)

</div>

A robust, enterprise-grade automated functional testing framework for **GroceryMate** (https://grocerymate.masterschool.com) built with **Python**, **Selenium WebDriver**, and **Pytest**. This framework implements the **Page Object Model (POM)** design pattern to ensure maximum code reusability, maintainability, and clean separation between test logic and UI interactions.

**Special Feature:** 🐛 **Bug Verifier Tests** that track active regressions in a controlled "Green/Success" monitoring state, allowing QA teams to monitor known issues without failing the entire test suite. Currently tracking 3 active bugs (BUG-001, BUG-003, BUG-004).

---

## 🎯 Quick Links

| Link | Description |
|------|-------------|
| **[GitHub Repository](https://github.com/abhisakh/selenium_pytest_project)** | Project source code |
| **[Live Application](https://grocerymate.masterschool.com)** | GroceryMate e-commerce site |
| **[Contact](mailto:abhisakh@gmail.com)** | abhisakh@gmail.com |

---

## 📚 Table of Contents

<details open>
<summary><b>✨ Click to expand/collapse table of contents</b></summary>

- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📂 Project Structure](#-project-structure)
- [⚙️ Prerequisites & Installation](#️-prerequisites--installation)
- [🔧 Configuration](#-configuration)
- [📄 Page Objects](#-page-objects)
- [🧪 Test Suites](#-test-suites)
- [🐛 Bug Tracking & Verification](#-bug-tracking--verification-strategy)
- [🚀 Execution & Reporting](#-execution--reporting)
- [💡 Best Practices](#-best-practices)
- [🔍 Troubleshooting](#-troubleshooting)
- [📝 Contributing](#-contributing)
- [🔄 CI/CD Integration](#️-cicd-integration)
- [🏗️ Architecture & Tech Stack Portfolio](#️-architecture--tech-stack-portfolio)
- [📄 License](#-license)

</details>

---

## ✨ Features

<div align="center">

### Core Capabilities

</div>

| Feature | Description | Benefit |
|---------|-------------|---------|
| 🏗️ **Page Object Model (POM)** | Encapsulates UI elements and interactions in dedicated page classes | Maximum code reusability & maintainability |
| 🧪 **Pytest Framework** | Powerful test execution with fixtures, markers, and plugins | Advanced test organization & execution control |
| 🐛 **Bug Verifiers** | Track known issues without failing critical test runs | Continuous monitoring of regressions |
| 📊 **HTML Reports** | Comprehensive test execution reports with bug tracking metrics | Visual test results & trend analysis |
| 🔄 **WebDriver Management** | Automatic browser initialization and cleanup via conftest.py | Reliable browser session management |
| 🛠️ **Reusable Utilities** | Helper functions for common operations (waits, scrolling, clicking) | DRY principle & code efficiency |
| ⚙️ **Environment Configuration** | Easy switching between staging, testing, and production environments | Flexible deployment options |
| 📸 **Logging & Screenshots** | Capture test execution flow and failure screenshots automatically | Enhanced debugging & test documentation |
| ⚡ **Parallel Execution** | Support for running tests in parallel using pytest-xdist | Faster test execution time |
| 🌐 **Cross-browser Testing** | Support for Chrome, Firefox, Safari, and Edge | Multi-browser compatibility verification |
| 📈 **Metrics & Analytics** | Test coverage, execution trends, bug tracking metrics | Data-driven QA insights |
| 🔐 **CI/CD Integration** | GitHub Actions workflows for automated testing | Continuous quality assurance pipeline |

---

## 🛠️ Tech Stack

<div align="center">

| Category | Technology | Version | Badge |
|----------|-----------|---------|-------|
| **Language** | Python | 3.8+ | ![Python](https://img.shields.io/badge/Python-3776ab?style=flat&logo=python&logoColor=white) |
| **Browser Automation** | Selenium WebDriver | 4.44.0 | ![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=flat&logo=selenium&logoColor=white) |
| **Testing Framework** | Pytest | 9.0.3 | ![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat&logo=pytest&logoColor=white) |
| **Test Reporting** | Pytest-HTML | 4.2.0 | ![HTML](https://img.shields.io/badge/HTML5-E34C26?style=flat&logo=html5&logoColor=white) |
| **Code Coverage** | Pytest-Cov | Latest | ![Coverage](https://img.shields.io/badge/Coverage-00C7B7?style=flat&logo=codecov&logoColor=white) |
| **Version Control** | Git/GitHub | Latest | ![Git](https://img.shields.io/badge/Git-F05032?style=flat&logo=git&logoColor=white) |
| **CI/CD** | GitHub Actions | Native | ![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat&logo=github-actions&logoColor=white) |
| **Pattern** | POM | v1.0 | ![POM](https://img.shields.io/badge/Page%20Object%20Model-00AA00?style=flat) |
| **License** | MIT | 2024 | ![MIT](https://img.shields.io/badge/MIT-green?style=flat) |

</div>

### Technology Stack Details

<div align="center">

```
┌─────────────────────────────────────────────────────────┐
│           GROCERYMATE QA AUTOMATION STACK               │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  🐍 Python 3.8+  ──────────────┐                       │
│                                 │                       │
│  🌐 Selenium 4.44.0  ──────────├──→ Browser Control    │
│     Chrome, Firefox             │                       │
│                                 │                       │
│  🧪 Pytest 9.0.3  ─────────────┤                       │
│     Fixtures, Markers           │                       │
│     Parametrization             ├──→ Test Execution    │
│                                 │                       │
│  📊 Pytest-HTML 4.2.0  ─────────┤                       │
│     Visual Reports              │                       │
│                                 │                       │
│  🔄 GitHub Actions  ────────────┤                       │
│     CI/CD Pipeline              ├──→ Automation        │
│     Auto Testing                │                       │
│                                 │                       │
│  📋 POM Design Pattern  ────────┘                       │
│     Page Objects                                        │
│     Reusable Components                                 │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

</div>

---

## 📂 Project Structure

```
selenium_pytest_project/
├── README.md                              # Project documentation
├── requirements.txt                       # Python dependencies
├── pytest.ini                             # Pytest configuration
├── .gitignore                             # Git ignore rules
│
├── pages/                                 # Page Object classes
│   ├── age_verification_page.py          # Age verification modal
│   ├── cart_page.py                      # Shopping cart operations
│   ├── login_page.py                     # User authentication
│   ├── product_page.py                   # Product details & reviews
│   ├── registration_page.py              # User signup form
│   └── store_page.py                     # Product listing
│
├── tests/                                 # Test suites
│   ├── conftest.py                       # Pytest fixtures
│   ├── test_age_verification.py          # Age gate tests
│   ├── test_login.py                     # Login tests
│   ├── test_registration.py              # Registration tests
│   ├── test_product_rating.py            # Review tests (BUG-001, BUG-004)
│   └── test_shipping.py                  # Shipping tests (BUG-003)
│
├── utils/                                 # Utilities
│   ├── constants.py                      # Configuration & constants
│   └── helpers.py                        # Helper functions
│
├── reports/                               # Generated reports
│   ├── test_report.html                  # HTML test report
│   ├── bug_report.html                   # Bug tracking report
│   ├── screenshots/                      # Failure screenshots
│   └── logs/                             # Execution logs
│
├── .github/
│   └── workflows/
│       └── automated-tests.yml           # GitHub Actions CI/CD
│
└── LICENSE                                # MIT License

```

---

## ⚙️ Prerequisites & Installation

### System Requirements

- **Python**: 3.8 or higher
- **pip**: Package manager
- **Browser Drivers**: ChromeDriver (for Chrome automation)
- **OS**: Windows, macOS, or Linux

### Step 1: Clone the Repository

```bash
git clone https://github.com/abhisakh/selenium_pytest_project.git
cd selenium_pytest_project
```

### Step 2: Set Up Python Virtual Environment

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
# Upgrade pip to latest version
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt
```

### Step 4: Download WebDriver

#### Option A: Automatic Installation (Recommended)

```bash
# Install webdriver-manager
pip install webdriver-manager

# Update conftest.py to use it:
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```

#### Option B: Manual Installation

1. **Check your Chrome version:**
   ```bash
   google-chrome --version  # macOS/Linux
   # OR
   "C:\Program Files\Google\Chrome\Application\chrome.exe" --version  # Windows
   ```

2. **Download matching ChromeDriver:**
   - Visit: [ChromeDriver Downloads](https://chromedriver.chromium.org/)
   - Download the version matching your Chrome browser

3. **Place ChromeDriver in PATH:**
   ```bash
   mv ~/Downloads/chromedriver /usr/local/bin/
   chmod +x /usr/local/bin/chromedriver
   ```

### Step 5: Verify Installation

```bash
# Check Python version
python --version

# Check installed packages
pip list

# Run a sample test
python -m pytest tests/test_login.py -v
```

---

## 🔧 Configuration

### utils/constants.py

```python
# Base URL Configuration
BASE_URL = "https://grocerymate.masterschool.com"
STORE_URL = f"{BASE_URL}/store"

# Test Account Credentials
USER_EMAIL = "abhisakh_3@gmail.com"
USER_PASS = "Falguni1982"

# Shipping Thresholds
SHIPPING_THRESHOLD = 20.00
STANDARD_SHIPPING_FEE = 5.00

# Error Messages
ERR_AGE_DENIED = "You are underage. You can still browse the site, but you will not be able to view alcohol products."
ERR_MAX_CHAR = "Feedback cannot exceed 500 characters."
```

### pytest.ini

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*

markers =
    smoke: Quick smoke tests
    regression: Full regression suite
    bug_tracker: Bug verification tests
    critical: Critical functionality tests

addopts = -v --strict-markers --tb=short
```

---

## 📄 Page Objects

Each page object encapsulates all UI elements and interactions for a specific page:

### Page Objects Included

#### 1. **Age Verification Page** (`pages/age_verification_page.py`)
- Handles age verification modal
- Locators for age input, confirmation button
- Methods for entering age and confirming

**Key Methods:**
```python
def navigate_to_store()         # Navigate to store page
def is_modal_visible()          # Check if modal is visible
def enter_dob(dob_string)      # Enter date of birth
def get_error_message()        # Get error message
```

#### 2. **Login Page** (`pages/login_page.py`)
- Email/Username field
- Password field
- Login button
- Error message display

**Key Methods:**
```python
def login(email, password)      # Perform user login
```

#### 3. **Registration Page** (`pages/registration_page.py`)
- Form fields (name, email, password, confirm password)
- Terms & conditions checkbox
- Submit button
- Validation error messages

**Key Methods:**
```python
def navigate_to_signup()        # Navigate to signup form
def register_user(name, email, password)  # Register new user
def get_success_message()       # Get success toast message
```

#### 4. **Store Page** (`pages/store_page.py`)
- Product list/grid
- Search functionality
- Pagination handling
- Add to cart button

**Key Methods:**
```python
def select_product_by_name(product_name)   # Select product
def add_product_to_cart(product_name)      # Add to cart
def _navigate_to_next_page(product_name)   # Handle pagination
```

#### 5. **Product Page** (`pages/product_page.py`)
- Product details (name, price, description)
- Image gallery
- Rating & reviews section
- Add to cart button
- **BUG TRACKING**: Review character limit, posted review rendering

**Key Methods:**
```python
def get_restriction_message()   # Get restriction message
def open_review_form()          # Open review form
def is_form_available()         # Check form availability
def select_rating(rating)       # Select star rating
def enter_review_text(text)     # Enter review text
def get_counter_value()         # Get character counter
def click_send()                # Submit review
```

#### 6. **Cart Page** (`pages/cart_page.py`)
- Cart item list
- Quantity adjustment
- Remove item button
- Subtotal, taxes, shipping cost calculation
- Checkout button
- **BUG TRACKING**: Shipping cost recalculation

**Key Methods:**
```python
def go_to_cart()                # Navigate to cart
def get_shipping_fee()          # Get shipping cost
def get_product_total()         # Get product total
def get_threshold_message()     # Get free shipping message
def complete_checkout(...)      # Complete checkout form
def clear_entire_cart()         # Clear cart items
```

---

## 🧪 Test Suites

### Test Execution Strategy

Each test file is organized by functionality and includes setup/teardown fixtures:

#### 1. **test_age_verification.py**
```
✓ Test age gate appears on first visit
✓ Test valid age entry passes verification
✓ Test invalid age entry fails verification
✓ Test boundary values (exact 18, underage, adult 25, child 14)
✓ Test empty input handling
✓ Test invalid format handling
```

#### 2. **test_login.py**
```
✓ Test login with valid credentials
✓ Test login error handling
✓ Test URL change after successful login
```

#### 3. **test_registration.py**
```
✓ Test successful user registration
✓ Test unique user generation
✓ Test registration success message
```

#### 4. **test_product_rating.py** ⚠️ **BUG TRACKERS**
```
✓ Test leave product review (BUG-001, BUG-004)
✓ Test valid rating after purchase
✓ Test error when submitting without stars
✓ Test review creation character boundaries
→ BUG-001: Character limit bypass (inverted assertion)
→ BUG-004: Posted review rendering (inverted assertion)
✓ Test edit existing review
✓ Test delete review
✓ Test review sort by rating
```

#### 5. **test_shipping.py** ⚠️ **BUG TRACKER**
```
✓ Test free shipping threshold
→ BUG-003: Shipping cost sticky state (inverted assertion)
✓ Test shipping cost calculation (BVA)
✓ Test empty cart scenario
✓ Test different shipping methods
✓ Test international shipping
```

---

## 🐛 Bug Tracking & Verification Strategy

This framework implements **Inverted Bug Verifiers** for known active issues. Unlike traditional tests that fail when a bug is present, these tests pass when the bug is confirmed to exist.

### How It Works

```
NORMAL TEST:         BUG VERIFIER TEST:
Code Works ✓ PASS    Bug Exists ✓ PASS (Green - Bug Confirmed)
Code Works ✗ FAIL    Bug Exists ✗ FAIL (Red - Bug Fixed)
Code Broken ✓ FAIL   Bug Missing ✓ FAIL (Red - Bug Patched)
Code Broken ✗ FAIL   Bug Missing ✗ FAIL (Red - Bug Patched)
```

### Active Bugs Monitored

#### **BUG-001: Character Limit Bypass** 🔴
- **File**: `tests/test_product_rating.py`
- **Severity**: Medium
- **Description**: Review edit modal incorrectly permits text submissions longer than 500 characters
- **Expected Behavior**: Form should reject entries > 500 characters
- **Current Behavior**: Form accepts strings up to 550+ characters
- **Test Status**: ✅ PASSING (Bug Confirmed - Green)
- **Test Function**: `test_review_edit_character_limit_bypass_bug_001()`
- **Verification Method**:
  ```python
  # Submit review with 550+ characters
  # Assert that text was saved with full length (confirming bug exists)
  assert actual_saved_length > 500
  ```

#### **BUG-003: Shipping Calculation Sticky State** 🔴
- **File**: `tests/test_shipping.py`
- **Severity**: High
- **Description**: Reducing cart items below €20 fails to reset shipping cost back to €5, keeping it stuck at €0
- **Expected Behavior**: When cart total < €20, shipping should be €5
- **Current Behavior**: Once free shipping is applied (total ≥ €20), removing items doesn't recalculate - stays at €0
- **Test Status**: ✅ PASSING (Bug Confirmed - Green)
- **Test Function**: `test_shipping_fee_reduction_calculation_bug_003()`
- **Verification Method**:
  ```python
  # Add items totaling €25 (free shipping)
  # Remove items down to €15 total
  # Assert shipping is still €0 (confirming bug exists)
  assert numeric_shipping == "0"
  ```

#### **BUG-004: UI String Visibility Blanking** 🔴
- **File**: `tests/test_product_rating.py`
- **Severity**: Medium
- **Description**: Successfully posted reviews incorrectly render as empty string nodes in the DOM
- **Expected Behavior**: Posted reviews should display review text in UI
- **Current Behavior**: Review exists in DOM but displays as blank/empty string
- **Test Status**: ✅ PASSING (Bug Confirmed - Green)
- **Test Function**: `test_posted_review_returns_empty_string_bug_004()`
- **Verification Method**:
  ```python
  # Submit review with text "This is a valid test review text..."
  # Assert posted review text is empty string (confirming bug exists)
  assert actual_text == ""
  ```

### Bug Verification Markers

Tag tests with `@pytest.mark.bug_tracker` for easy filtering:

```bash
# Run only bug trackers
python -m pytest -m bug_tracker

# Run all except bug trackers
python -m pytest -m "not bug_tracker"
```

---

## 🚀 Execution & Reporting

### Basic Test Execution

#### Run All Tests & Generate HTML Report
```bash
python -m pytest tests/ --html=reports/test_report.html --self-contained-html -v
```

#### Run Specific Test File
```bash
python -m pytest tests/test_login.py -v
```

#### Run Specific Test Function
```bash
python -m pytest tests/test_login.py::TestLoginPage::test_login_valid_credentials -v
```

#### Run Tests by Marker
```bash
# Smoke tests only
python -m pytest -m smoke -v

# Regression tests only
python -m pytest -m regression -v

# Bug tracker tests only
python -m pytest -m bug_tracker -v

# Exclude bug trackers
python -m pytest -m "not bug_tracker" -v
```

#### Run Tests with Specific Keyword
```bash
python -m pytest -k "login" -v
```

### Advanced Execution Options

#### Parallel Test Execution
```bash
# Install pytest-xdist
pip install pytest-xdist

# Run 4 tests in parallel
python -m pytest tests/ -n 4

# Auto-detect CPU count
python -m pytest tests/ -n auto
```

#### Capture Output & Verbose Logging
```bash
python -m pytest tests/ -v -s --tb=short
```

#### Generate Multiple Report Formats
```bash
# HTML Report
python -m pytest tests/ --html=reports/test_report.html --self-contained-html

# JUnit XML (for CI/CD)
python -m pytest tests/ --junit-xml=reports/junit.xml

# Coverage Report
python -m pytest tests/ --cov=. --cov-report=html
```

### Generated Reports

Reports are automatically saved to `reports/` directory:

- **test_report.html**: Interactive HTML test report
- **bug_report.html**: Bug tracking report with metrics
- **junit.xml**: Machine-readable format for CI/CD
- **screenshots/**: Failure screenshots (automatic)
- **logs/**: Detailed execution logs

---

## 💡 Best Practices

### 1. **Naming Conventions**

```python
# Page classes: <FunctionalityName>Page
class LoginPage(BasePage):
    pass

# Test classes: Test<PageName>
class TestLoginPage:
    pass

# Test methods: test_<specific_functionality>
def test_login_with_valid_credentials(self):
    pass

# Locators: use descriptive names
LOGIN_BUTTON = (By.ID, "login-btn")
EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
```

### 2. **Locator Strategy**

Prefer in this order:
1. **ID** - Most stable and fast
2. **Name** - Good for form elements
3. **CSS Selector** - Flexible and readable
4. **XPath** - Last resort (fragile)

```python
# Good ✓
(By.ID, "submit-button")
(By.CSS_SELECTOR, ".login-form input[type='email']")

# Avoid ✗
(By.XPATH, "/html/body/div[1]/div[2]/form/input")
```

### 3. **Explicit Waits Over Implicit**

```python
# Preferred ✓
wait = WebDriverWait(self.driver, 10)
element = wait.until(EC.presence_of_element_located(locator))

# Avoid ✗
self.driver.implicitly_wait(10)
element = self.driver.find_element(*locator)
```

### 4. **Test Independence**

- Each test should be independent and runnable in any order
- Use fixtures for setup/teardown
- Clean data after test execution

### 5. **DRY Principle - Don't Repeat Yourself**

- Use helper methods in BasePage for common operations
- Reuse page objects across test suites
- Create utility functions for repetitive actions

### 6. **Clear Assertions**

```python
# Good ✓
assert page.is_error_message_displayed(), "Error message not shown"
assert page.get_login_button_text() == "Sign In"

# Avoid ✗
assert page.login_button
assert page.error_message
```

### 7. **Logging & Screenshots**

```python
logger.info(f"User logging in with email: {email}")
if test_fails:
    self.driver.save_screenshot("failure_screenshot.png")
logger.error(f"Login failed: {error_message}")
```

---

## 🔍 Troubleshooting

### Issue: ModuleNotFoundError
**Problem**: Import errors when running tests
```bash
ModuleNotFoundError: No module named 'pages'
```

**Solution**: Always run pytest with python -m flag
```bash
python -m pytest tests/
# NOT: pytest tests/
```

### Issue: ChromeDriver Version Mismatch
**Problem**: WebDriver version doesn't match Chrome browser
```bash
selenium.common.exceptions.SessionNotCreatedException
```

**Solution**:
1. Check your Chrome version: `chrome://version/`
2. Download matching ChromeDriver from [chromedriver.chromium.org](https://chromedriver.chromium.org/)
3. Update path in `utils/constants.py`

### Issue: Element Not Found
**Problem**: Locators timing out or elements not visible
```bash
TimeoutException: Message: timeout
NoSuchElementException: no such element
```

**Solutions**:
- Increase `EXPLICIT_WAIT` timeout in constants.py
- Add explicit waits before interactions
- Verify locators are correct using browser DevTools
- Check for iframe switching requirements

### Issue: Tests Flaky/Inconsistent
**Problem**: Tests pass sometimes, fail other times

**Solutions**:
- Replace implicit waits with explicit waits
- Add proper visibility checks before clicking
- Implement retry logic for flaky assertions
- Reduce test parallelization if resource constrained

---

## 📝 Contributing

### Code Style

- Follow PEP 8 guidelines
- Use descriptive variable names
- Add docstrings to functions

```python
def login(self, email: str, password: str) -> None:
    """
    Performs user login with email and password.

    Args:
        email (str): User email address
        password (str): User password

    Raises:
        TimeoutException: If login form doesn't appear within timeout
    """
    self.wait_and_click(self.EMAIL_INPUT)
    self.send_keys(self.EMAIL_INPUT, email)
    self.send_keys(self.PASSWORD_INPUT, password)
    self.wait_and_click(self.LOGIN_BUTTON)
```

### Adding New Tests

1. Create test file in `tests/` directory: `test_feature_name.py`
2. Inherit from appropriate page object
3. Add pytest markers: `@pytest.mark.regression`
4. Include clear test naming and docstrings
5. Implement proper setup/teardown with fixtures

### Adding New Page Objects

1. Create new file: `pages/new_page.py`
2. Inherit from `BasePage`
3. Define all locators at class level
4. Implement action methods
5. Add docstrings for all methods

### Commit Guidelines

Write clear, descriptive commit messages:

```bash
# ✅ GOOD: Clear and descriptive
git commit -m "feat: Add product search page object and tests"
git commit -m "fix: Resolve flaky age verification test with explicit wait"
git commit -m "docs: Update README with bug tracking guidelines"
git commit -m "test: Add parametrized tests for shipping cost calculation"

# ❌ BAD: Vague and unclear
git commit -m "fixes"
git commit -m "update stuff"
git commit -m "working now"
```

### Commit Message Format

```
<type>: <subject>

<body>

<footer>
```

**Types:**
- `feat:` New feature or page object
- `fix:` Bug fix in code or tests
- `test:` New tests or test improvements
- `docs:` Documentation updates
- `refactor:` Code restructuring
- `chore:` Dependency updates, tooling

### Pull Request Process

1. **Run all tests locally**
   ```bash
   python -m pytest tests/ -v
   ```

2. **Run only your changes**
   ```bash
   python -m pytest tests/test_your_feature.py -v
   ```

3. **Update documentation** if needed
   - Update README if adding features
   - Add docstrings to new functions
   - Comment complex logic

### PR Template

When submitting a PR, include:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Test improvement

## Related Issues
Closes #issue_number

## Testing
- [ ] All tests pass locally
- [ ] Added new tests
- [ ] Verified no regressions

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex logic
- [ ] Documentation updated
```

---

## 🔄 CI/CD Integration

### GitHub Actions Workflow

Create `.github/workflows/automated-tests.yml`:

```yaml
name: Automated QA Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM UTC

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ['3.8', '3.9', '3.10']

    steps:
    - uses: actions/checkout@v3
    - uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install Chrome and ChromeDriver
      run: |
        # Install Chrome
        # Install matching ChromeDriver

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: |
        mkdir -p reports
        python -m pytest tests/ --html=reports/test_report.html --self-contained-html -v

    - name: Upload reports
      uses: actions/upload-artifact@v3
      if: always()
      with:
        name: test-reports
        path: reports/
```

### Jenkins Integration

Configure Jenkins pipeline to:
1. Clone repository
2. Install dependencies
3. Run pytest with HTML report generation
4. Archive test reports
5. Publish JUnit results

---

## 🏗️ Architecture & Tech Stack Portfolio

### Complete Technology Stack

#### Frontend Testing & UI Automation
```
🌐 Selenium WebDriver 4.44.0
   ├── Chrome Driver
   ├── Firefox Driver
   ├── Safari Driver
   └── Edge Driver
```

#### Test Framework & Execution
```
🧪 Pytest 9.0.3 (Core Testing)
   ├── Fixtures (conftest.py)
   ├── Markers (smoke, regression, bug_tracker)
   ├── Parametrization
   ├── Plugins Support
   └── xdist (Parallel Execution)

📊 Pytest-HTML 4.2.0 (Test Reports)
   ├── Visual Test Reports
   ├── Test Metadata
   └── Screenshots on Failure
```

#### Design Pattern
```
📐 Page Object Model (POM) v1.0
   ├── pages/ Directory
   │   ├── Base Page Class
   │   ├── Page-specific Classes
   │   └── Locator Definitions
   │
   ├── tests/ Directory
   │   ├── Test Classes
   │   ├── Test Methods
   │   └── Test Fixtures
   │
   └── utils/ Directory
       ├── Constants & Configuration
       └── Helper Functions
```

### Project Statistics

| Metric | Value |
|--------|-------|
| **Total Test Cases** | 20+ |
| **Test Classes** | 6 |
| **Page Objects** | 6 |
| **Bugs Tracked** | 3 (BUG-001, BUG-003, BUG-004) |
| **CI/CD Jobs** | 2 (Main + Bug Tracker) |
| **Python Versions** | 3 (3.8, 3.9, 3.10) |
| **Documentation Files** | 1 (Unified README) |
| **Code Examples** | 50+ |
| **Test Markers** | 5 (smoke, regression, bug_tracker, critical, slow) |

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    GROCERYMATE QA FRAMEWORK                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  📊 Test Reports & Execution                         │  │
│  │  ├── HTML Reports (pytest-html)                      │  │
│  │  ├── JUnit XML (CI/CD)                               │  │
│  │  ├── Screenshots on Failure                          │  │
│  │  └── Execution Logs                                  │  │
│  └──────────────────────────────────────────────────────┘  │
│           ↑                                 ↑                │
│           │                                 │                │
│  ┌────────┴──────────┐         ┌───────────┴─────────┐     │
│  │  🧪 Test Layer   │         │  🐛 Bug Verifier    │     │
│  │  ├── conftest.py │         │  ├── BUG-001        │     │
│  │  ├── test_*.py   │         │  ├── BUG-003        │     │
│  │  └── Fixtures    │         │  └── BUG-004        │     │
│  └────────┬──────────┘         └───────────┬─────────┘     │
│           │                                 │                │
│           └────────────────┬────────────────┘                │
│                            │                                │
│                    ┌──────▼──────┐                         │
│                    │ 📄 Page     │                         │
│                    │ Objects     │                         │
│                    │ (POM)       │                         │
│                    ├─────────────┤                         │
│                    │ Pages/      │                         │
│                    │ ├── age_... │                         │
│                    │ ├── login_..│                         │
│                    │ ├── product_│                         │
│                    │ ├── cart_...│                         │
│                    │ ├── store_..│                         │
│                    │ └── reg_... │                         │
│                    └──────┬──────┘                         │
│                           │                                 │
│                    ┌──────▼──────────────┐                 │
│                    │ 🌐 Selenium        │                 │
│                    │ WebDriver          │                 │
│                    │                    │                 │
│                    │ Chrome | Firefox   │                 │
│                    │ Safari | Edge      │                 │
│                    └──────┬──────────────┘                 │
│                           │                                 │
│                    ┌──────▼──────────────┐                 │
│                    │ 🍎 GroceryMate      │                 │
│                    │ Application         │                 │
│                    │                    │                 │
│                    │ https://grocery...  │                 │
│                    └────────────────────┘                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Development Workflow

```
Local Development          GitHub                CI/CD
─────────────────────      ──────                ─────

1. Feature Branch  ──push──→ Pull Request
   feature/*                ↓
                          Reviews
2. Write Tests     ──────→ Approval
   test_*.py                ↓
                         Merge to main
3. Local Testing   ──────→ ↓
   pytest                 GitHub Actions
   python -m ...         Triggered ──→ Run Tests
                                       Generate Reports
4. Commit & Push           ↓
   git commit            Status Check ← Results
   git push              ✅ PASS / ❌ FAIL
```

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

**Copyright © 2024 Abhisakh Sharma**

---

## 📞 Support & Contact

- **GitHub**: https://github.com/abhisakh
- **Email**: abhisakh@gmail.com
- **Project**: GroceryMate QA Automation Framework

---

## ✨ Key Strengths

| Strength | Benefit |
|----------|---------|
| **Page Object Model** | Easy maintenance & code reuse |
| **Pytest Framework** | Flexible & extensible testing |
| **Bug Verifiers** | Continuous regression tracking |
| **CI/CD Integration** | Automated quality assurance |
| **Comprehensive Docs** | Easy onboarding for new team members |
| **Cross-browser Support** | Multi-platform compatibility testing |
| **Parallel Execution** | Fast feedback loop |
| **Visual Reports** | Clear test results & trends |

---

## 📈 Project Maturity

| Aspect | Maturity | Status |
|--------|----------|--------|
| Test Coverage | High | ✅ 20+ test cases |
| Code Quality | Professional | ✅ PEP 8 compliant |
| Documentation | Excellent | ✅ Comprehensive |
| CI/CD Setup | Production-ready | ✅ GitHub Actions |
| Bug Tracking | Active | ✅ 3 monitored bugs |
| Maintainability | High | ✅ POM pattern |
| Scalability | Good | ✅ Parallel execution |

---

**Last Updated**: June 2024
**Framework Version**: 1.0
**Status**: Production Ready ✅

**Created with ❤️ for Quality Assurance Excellence**
