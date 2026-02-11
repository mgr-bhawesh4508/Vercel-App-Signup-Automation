# Vercel App Signup Automation

This project automates the signup flow of a web application using Python, Selenium WebDriver, and PyTest. It covers user registration, OTP verification using temporary email, multi-step form submission, and file upload validation.

---

## Tech Stack & Environment

- Programming Language: Python 3.12
- Automation Framework: Selenium WebDriver
- Test Framework: PyTest
- Browser: Google Chrome (v143 or compatible)
- OS: Windows
- For Reports: Java, Scoop and Allure
- Design Pattern: Page Object Model (POM)

---

## Prerequisites

- Python 3.10 or above installed
- Google Chrome installed
- ChromeDriver (compatible with your Chrome version)
- Git installed
- Java installed (for Allure reports)
- Scoop installed (for installing Allure on Windows)
- Allure installed
- Virtual Environment (venv)

---

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/mgr-bhawesh4508/Vercel-App-Signup-Automation.git


### 2. Navigate to project directory

cd VercelAppSignupAutomation


### 3. Create and activate virtual environment

python -m venv venv
venv\Scripts\activate


### 4. Install dependencies

pip install -r requirements.txt


---

## How to Run the Tests

To execute test cases, run:

pytest -v


To generate report, run:

pytest --alluredir=allure-results


To view report, run:

allure serve allure-results


---

## Test Scenarios Covered

- User signup with valid details
- Privacy policy acceptance validation
- OTP verification using temporary email
- Multi-step agency information form
- File upload validation
- Successful account creation flow

---

## Test Data & OTP Handling

- Temporary email accounts are used for OTP verification.
- Dummy data is used for user and agency details.
- OTP is automatically fetched from the temporary email inbox using the `requests` library.
- The OTP is dynamically extracted during test execution to complete verification.

---

## Important Configuration Before Running

If you run tests multiple times or on a new system, update the following:

### 1. Update Phone Number

Modify in:

data/test_data.py


Each execution requires a unique phone number to avoid duplication errors.

---

### 2. Update File Path for Upload

Set your actual file path in:

utils/upload_file.py


Example:

file_path = "C:/Users/YourName/Documents/sample.pdf"


---

### 3. Update ChromeDriver Path

Set your actual ChromeDriver path in:

utils/test_runner.py


Example:

service = Service("C:/Users/YourName/Downloads/chromedriver.exe")


Ensure ChromeDriver version matches your Chrome browser version.

---

---

## Framework Architecture

- `base_page.py` contains reusable Selenium methods.
- `signup_page.py` contains signup-specific locators and actions.
- `assertion.py` contains reusable assertion utilities.
- `otp_reader.py` handles OTP retrieval using HTTP requests.
- `upload_file.py` manages file upload functionality.
- `test_runner.py` initializes and configures WebDriver.

---

## Reporting

Allure reporting provides:

- Detailed execution reports
- Step-level tracking
- Failure screenshots
- Execution summary dashboard

---

## Author

Automation framework developed to validate a real-world signup flow using Selenium WebDriver and PyTest following industry best practices.
