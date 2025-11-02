from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")
        self.user_dropdown = (By.CLASS_NAME, "oxd-userdropdown-tab")
        # updated to match your HTML exactly
        self.logout_button = (By.XPATH, "//a[@class='oxd-userdropdown-link' and contains(@href,'logout')]")

    def is_loaded(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.dashboard_header))
            return True
        except:
            return False

    def logout(self):
        # click user dropdown to open the menu
        self.wait.until(EC.element_to_be_clickable(self.user_dropdown)).click()
        # short delay to let React menu appear
        time.sleep(1)
        # wait for the logout link and click it
        self.wait.until(EC.element_to_be_clickable(self.logout_button)).click()
