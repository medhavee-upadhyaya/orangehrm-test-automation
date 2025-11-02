from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Updated locators (verified on 2025 OrangeHRM demo)
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button  = (By.XPATH, "//button[@type='submit']")
        self.error_banner  = (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")
        self.dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password):
        # Wait until Username input is visible
        self.wait.until(EC.visibility_of_element_located(self.username_input))
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)

        self.wait.until(EC.visibility_of_element_located(self.password_input))
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)

        self.driver.find_element(*self.login_button).click()

    def is_dashboard_visible(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.dashboard_header))
            return True
        except:
            return False

    def get_error_message(self):
        try:
            element = self.wait.until(EC.visibility_of_element_located(self.error_banner))
            return element.text
        except:
            return None
