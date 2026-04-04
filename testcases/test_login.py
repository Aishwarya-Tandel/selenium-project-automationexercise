import json

import pytest
from pageobject.basepage import Common_Base_Page
from pageobject.page_login import Login
from utility.logging_log import Log_store
from utility.failed_screenshot import Screenshot_Capture


#read json file
with open(r"C:\Users\LENOVO\PycharmProjects\selenium-project-automationexercise\testdata\login_data.json") as login_file :
    data = json.load(login_file)
    test_data = data["login"]

@pytest.mark.parametrize("login_test_data_list" , test_data)
class Test_Login:
    def test_login(self,setup_teardown,login_test_data_list):
        driver =  setup_teardown

        log = Log_store.get_log(__name__)

        log.info("*********** Login Test Starts ***********")

        driver.get("https://automationexercise.com/")

        #click on login/signup menu
        #as it is from another folder/file/class so make object and use that method
        base = Common_Base_Page(driver)
        log.debug("successfully clicked on login/signup")
        base.signup_login_menu()
        log.debug("landed to login menu")

        #now fill login details
        log_in =  Login(driver)
        log_in.login(login_test_data_list["email"] , login_test_data_list["password"])
        log.debug("entered username and password")

        if login_test_data_list["scenario_success"] == 'correct' :
            assert  log_in.login_success()
        else:
            error = log_in.login_error_message()
            Screenshot_Capture.failed_screenshot_capture(driver,"invalid_login") #take screenshot
            assert 'incorrect' in error # do assertion/validation
            log.error(f"login test failed because {error}")

        log.info("*********** Login Test Ends ***********")


