import time

from pageobject.basepage import Common_Base_Page
from pageobject.page_login import Login
from pageobject.home_page import HomePage

from pageobject.page_login import Login
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pageobject.page_product_details import ProductDetails
from pageobject.page_product_search import ProductSearch

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
        driver.maximize_window()

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

# fixture for pre-requisite logic for search product
@pytest.fixture
def already_searched_logic(setup_teardown,request):
    driver=setup_teardown

    data = request.param

    # click on product menu
    home = HomePage(driver)
    home.products_menu()

    # type product name to search
    search = ProductSearch(driver)
    search.click_on_search_item(data)

    # click on search button
    search.click_on_search_button()

    # wait till search done
    base = Common_Base_Page(driver)
    base.wait_for_visibility(search.searched_done)

    return driver ,search  # in one of the test file "test_submit_review_of_product", i want to use driver as well along with search so returned both

@pytest.fixture
def already_reached_product_details_page_logic(already_searched_logic):
    # we need details till setup_teardown + already_searched_logic
    # but already_searched_logic fixture already having setup_teardown so directly use already_searched_logic
    driver , search = already_searched_logic # this fixture return two so store in 2 variable

    """
    data = request.param  - we are not using it 
    because we are receiving data from test for fixture "already_searched_logic"
    
    so even we are not using data here but we need for "already_searched_logic" fixture
    so in parametrize pass "already_searched_logic" fixture name
    """

    # now click on view product
    search.product_names_and_click_on_view_product() #so instead this use search variable : already_searched_logic.product_names_and_click_on_view_product()

    #check successfully landed to product details page after clicked on view product
    search.is_successfully_reached_on_view_product()

    #after this we will land to product details page and for that page we have class "ProductDetails"
    # so better create object here only and return

    product_det = ProductDetails(driver)
    return product_det , search
