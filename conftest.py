import time

from pageobject.page_login import Login
from pageobject.home_page import HomePage

from pageobject.page_login import Login
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

    #2 get the value of given browser at command line
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
        driver.get("https://automationexercise.com/")

    except:
        raise Exception("not a valid browser name")

    yield driver

    driver.quit()



# fixture for pre-requisite logic for login
@pytest.fixture
def logged_in_user(setup_teardown , request):
    driver = setup_teardown

    #receive data from test using parametrize and we need email and password
    data = request.param

    #from landing page click on login/signup button
    login_btn = HomePage(driver)
    login_btn.signup_login_menu()

    #login logic
    login_l = Login(driver)
    login_l.login(data["email"] , data["password"])  # don't pass hardcoded email and pass. use parametrize

    login_l.login_success()

    # return driver
    # but as you know you will land to homepage where out loginbutton is there (means in home_page.py we have logout button)
    # so anyway after login you will land there , so you need to create object of it to call logot() in test method also
    # and whereever you will use you need to create same home_page.py's HopePge class object
    # so better to avoid duplicate code , create object here and return that , rather than return driver

    home = HomePage(driver)
    return home


