# OrangeHRM QA Automation Framework (Selenium + Pytest)

## Overview
This project is a complete QA automation framework designed to test the OrangeHRM Demo web application (https://opensource-demo.orangehrmlive.com/).

It covers:
- Functional Smoke Tests (Login, Logout)
- PIM Module Tests (Employee Search – existing and non-existing records)
- Automatic Screenshot Capture
- HTML Report Generation (with detailed test results)

The framework is built using the **Page Object Model (POM)** pattern and **Pytest** for scalability and maintainability.


## Tech Stack
- **Language:** Python 3.10+
- **Framework:** Pytest
- **UI Automation:** Selenium WebDriver
- **Reporting:** Pytest-HTML, Allure Reports
- **Design Pattern:** Page Object Model (POM)
- **CI/CD Ready:** Easily integrable with Jenkins or GitHub Actions


## Folder Structure

orangehrm-qa-automation-medhavee/
├── config/
│   └── config.yaml
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── pim_page.py
├── tests/
│   ├── test_smoke_setup.py
│   ├── test_invalid_login.py
│   ├── test_logout.py
│   ├── test_search_employee.py
│   └── test_search_employee_negative.py
├── reports/
│   ├── full_suite.html
│   └── screenshots/
│       ├── sample_Peter.png
│       └── sample_NoRecord.png
├── conftest.py
├── requirements.txt
└── README.md


## How to Run Tests

1. Clone this repo  
   ```bash
   git clone https://github.com/<your-username>/orangehrm-qa-automation-medhavee.git
   cd orangehrm-qa-automation-medhavee

2. Create and activate a virtual    environment
    python3 -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      #Windows

3. Install dependencies
    pip install -r requirements.txt

4. Run all tests and generate HTML report
    pytest -v -s tests/ --html=reports/full_suite.html --self-contained-html

5. View your report
    open reports/full_suite.html


### Sample Output
Add screenshots or report snippet — this visual impresses instantly.

## Sample Reports & Screenshots

- **HTML Report Preview:**
  ![HTML Report](reports/screenshots/sample_report_preview.png)

- **Screenshot Example:**
  ![Employee Search Result](reports/screenshots/sample_Peter.png)


## Highlights
- Page Object Model (POM) for better code reusability
- Config-driven design (YAML-based configuration)
- Screenshot capture for every test outcome
- Positive + Negative test scenarios
- HTML reporting for management visibility
- Modular and scalable structure for CI/CD pipelines


## Future Enhancements
- Integrate with Jenkins for CI/CD automation
- Add Data-Driven Testing using CSV/Excel
- Expand coverage to Leave/Recruitment modules
- Generate Allure Reports for advanced analytics


## Author
**Medhavee Upadhyaya**  
Master’s in Computer Science | Software Engineer in Test  
[LinkedIn](www.linkedin.com/in/medhavee-upadhyaya) | [GitHub](https://github.com/medhavee-upadhyaya)

```markdown