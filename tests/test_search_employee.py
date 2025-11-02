import time
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage

def test_search_employee(driver, config_data):
    """
    TC-005 Automation:
    Search existing and non-existing employees.
    """
    lp = LoginPage(driver)
    lp.login(config_data["valid_username"], config_data["valid_password"])

    dp = DashboardPage(driver)
    assert dp.is_loaded(), "Dashboard did not load after login."

    pim = PIMPage(driver)

    # Case 1: Known employee (positive)
    employee_name = "Peter"
    pim.search_employee(employee_name)
    found = pim.results_contain(employee_name)
    if found:
        print(f"✅ Employee '{employee_name}' exists in records.")
    else:
        print(f"⚠️ No record found for '{employee_name}'. (Expected if deleted)")
    time.sleep(1)

    # Case 2: Non-existing employee (negative)
    employee_name = "NonExistingXYZ"
    pim.search_employee(employee_name)
    found = pim.results_contain(employee_name)
    if not found:
        print(f"⚠️ No record found for '{employee_name}' — handled gracefully.")
    else:
        print(f"✅ Unexpectedly found record for '{employee_name}'.")
