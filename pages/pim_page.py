from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from datetime import datetime


class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        # Locators
        self.pim_tab = (By.XPATH, "//span[text()='PIM']")
        self.employee_name_input = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.search_button = (By.XPATH, "//button[normalize-space()='Search']")
        self.result_rows = (By.XPATH, "//div[@class='oxd-table-body']//div[@role='row']")
        self.no_records_label = (By.XPATH, "//span[contains(text(),'No Records Found')]")

    def search_employee(self, name):
        """Navigate to PIM, search employee by name."""
        self.wait.until(EC.element_to_be_clickable(self.pim_tab)).click()
        name_box = self.wait.until(EC.visibility_of_element_located(self.employee_name_input))
        name_box.clear()
        name_box.send_keys(name)
        self.wait.until(EC.element_to_be_clickable(self.search_button)).click()
        time.sleep(2)

    def results_contain(self, name):
        """Check if the employee appears in results or show 'No Records Found', with screenshots."""
        try:
            time.sleep(2)
            # Create absolute screenshot path
            screenshot_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "reports", "screenshots"))
            os.makedirs(screenshot_dir, exist_ok=True)

            # Unique filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")

            # Case 1: No Records Found
            if self.driver.find_elements(*self.no_records_label):
                print(f"⚠️ No record found for '{name}'. Screenshot saved: {screenshot_path}")
                self.driver.save_screenshot(screenshot_path)
                return False

            # Case 2: Record found
            rows = self.driver.find_elements(*self.result_rows)
            for row in rows:
                if name.lower() in row.text.lower():
                    print(f"✅ Record found for '{name}'. Screenshot saved: {screenshot_path}")
                    self.driver.save_screenshot(screenshot_path)
                    return True

            # Case 3: No match even if table is loaded
            print(f"⚠️ Table loaded but no match found for '{name}'. Screenshot saved: {screenshot_path}")
            self.driver.save_screenshot(screenshot_path)
            return False

        except Exception as e:
            print(f"❌ Error verifying search results: {e}")
            error_path = os.path.join(screenshot_dir, f"error_{timestamp}.png")
            self.driver.save_screenshot(error_path)
            print(f"🧾 Error screenshot saved: {error_path}")
            return False
