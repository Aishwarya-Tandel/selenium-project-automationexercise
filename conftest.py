import time

from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

"""At run time decide , need to run test on which browser ?
#1 - tell browser that this command exist
"""
def pytest_addoption(parser):
    parser.addoption("--browser",
                      default = 'chrome',
                      action = 'store')

@pytest.fixture
def setup_teardown(request):
    preferences = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False,
        "safebrowsing.enabled": False
    }

    #2 get the value of given browser at commnad line
    browser_name = request.config.getoption("--browser")
    try:
        if browser_name == 'chrome' :
            option = ChromeOptions()
            option.add_experimental_option("prefs",preferences)
            driver = webdriver.Chrome(options=option)
        if browser_name == 'edge':
            option = EdgeOptions()
            option.add_experimental_option("prefs",preferences)
            driver = webdriver.Edge(options=option)
        if browser_name == 'firefox':
            driver = webdriver.Firefox()

        driver.implicitly_wait(5)

    except:
        raise Exception("not a valid browser name")

    yield driver

    driver.quit()

