# Automated QA Testing Framework (POM)
This repository contains an automated functional testing framework built with Python, Selenium WebDriver, and Pytest. The project is designed using the Page Object Model (POM) pattern to maximize code reusability, maintainability, and clean separation between test logic and UI interactions.

In addition to standard functional verification, this test suite is configured with specialized Bug Verifier Tests that track active regressions in a controlled "Green/Success" monitoring state.

## 📂 Project Structure
```python
Plaintext
├── README.md                           # Project documentation
├── pages/                              # Page Object classes (UI locators & actions)
│   ├── age_verification_page.py
│   ├── cart_page.py
│   ├── login_page.py
│   ├── product_page.py
│   ├── registration_page.py
│   └── store_page.py
├── tests/                              # Test suites & execution hooks
│   ├── conftest.py                    # Shared fixtures (WebDriver setup)
│   ├── test_age_verification.py
│   ├── test_login.py
│   ├── test_product_rating.py         # Includes BUG-001 & BUG-004 Trackers
│   ├── test_registration.py
│   └── test_shipping.py               # Includes BUG-003 Tracker
├── utils/                              # Core utilities & configurations
│   ├── constants.py                    # Environment URLs and thresholds
│   └── helpers.py                      # Global setup/cleanup wrappers
└── reports/                            # Generated HTML execution metrics
    └── bug_report.html

```

## ⚙️ Prerequisites & Installation
** 1. Clone the Repository **
Bash
git clone <repository-url>
cd selenium_pytest_project
** 2. Set Up the Virtual Environment ** 
Bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
** 3. Install Dependencies ** 
Bash
pip install -r requirements.txt
Note: Ensure pytest and pytest-html are installed within your active virtual environment.

## 🧪 Bug Tracking & Verification Strategy
Unlike traditional tests that fail when a bug is present, this framework implements Inverted Bug Verifiers for known active issues.

Passing State (Green): Confirms that the target bug is successfully detected and still actively reproducible on the system.

Failing State (Red): Signals that the system behavior changed (likely meaning a developer patched the issue, requiring a rewrite to a standard regression assertion).

Target Bugs Monitored:
BUG-001 (Character Limit Bypass): Verifies that the review edit modal incorrectly permits text submissions longer than 500 characters.

BUG-003 (Shipping Calculation Sticky State): Verifies that reducing items below 20€ fails to reset the shipping cost back to 5€, keeping it stuck at 0€.

BUG-004 (UI String Visibility Blanking): Verifies that successfully posted reviews incorrectly render as empty string nodes in the DOM layout.

## 🚀 Execution & Reporting
To run tests safely without encountering pathing import errors (ModuleNotFoundError), always invoke pytest using the python -m flag. This guarantees that the root directory is appended to Python's search paths.

Run All Tests & Generate HTML Report
Bash
python -m pytest tests/ --html=reports/bug_report.html --self-contained-html
Run Product Rating Bug Trackers Only
Bash
python -m pytest tests/test_product_rating.py -v
Run Shipping Calculation Bug Trackers Only
Bash
python -m pytest tests/test_shipping.py -v
