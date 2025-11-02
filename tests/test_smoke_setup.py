from pages.login_page import LoginPage
import time

def test_valid_login_smoke(driver, config_data):
    """
    TC-001 Automation:
    Verify user can log in with valid Admin credentials
    and land on Dashboard.
    """

    lp = LoginPage(driver)

    lp.login(
        config_data["valid_username"],
        config_data["valid_password"]
    )

    # small wait just to let the dashboard load
    time.sleep(2)

    assert lp.is_dashboard_visible(), "Dashboard was not visible after login with valid creds"
