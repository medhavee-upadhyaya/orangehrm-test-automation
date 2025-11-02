import pytest
import yaml
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="session")
def config_data():
    """
    Load test configuration (URL, credentials, etc.)
    """
    with open("config/config.yaml", "r") as f:
        data = yaml.safe_load(f)
    return data

@pytest.fixture
def driver(config_data):
    """
    Spin up Chrome before each test and close after.
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get(config_data["base_url"])
    yield driver
    driver.quit()
 