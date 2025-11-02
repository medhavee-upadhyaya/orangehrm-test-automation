from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
import time

def test_logout(driver, config_data):
    """
    TC-004 Automation:
    Verify that user can log out successfully
    and session ends.
    """
    lp = LoginPage(driver)
    lp.login(config_data["valid_username"], config_data["valid_password"])
    dp = DashboardPage(driver)
    assert dp.is_loaded(), "Dashboard did not load after login"

    dp.logout()
    time.sleep(2)
    assert "login" in driver.current_url.lower(), "Logout did not redirect to login page"
