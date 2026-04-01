import time

from selenium import webdriver
import pytest

"""At run time decide , need to run test on which browser ?
#1 - tell browser that this command exist
"""
def pytest_addoption(parser):
    parser.addoption("--browser",
                      default = 'chrome',
                      action = 'store')

@pytest.fixture
def setup_teardown(request):

    #2 get the value of given browser at commnad line
    browser_name = request.config.getoption("--browser")
    try:
        if browser_name == 'chrome' :
            driver = webdriver.Chrome()
        if browser_name == 'edge':
            driver = webdriver.Edge()
        if browser_name == 'firefox':
            driver = webdriver.Firefox()

        driver.implicitly_wait(5)

    except:
        raise Exception("not a valid browser name")

    yield driver

    driver.quit()

