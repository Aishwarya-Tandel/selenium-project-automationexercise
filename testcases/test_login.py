import json
import time

import pytest

from pageobject.common_base_page import Common_Base_Page
from pageobject.page_login import Login
from utility.logging_log import Log_store

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
        log.debug("successfullly clicked on login/signup")
        base.signup_login_menu()
        log.debug("landed to login menu")

        #now fill login details
        log_in =  Login(driver)
        log_in.login(login_test_data_list["email"] , login_test_data_list["password"])
        log.debug("entered username and password")

        log.info("*********** Login Test Ends ***********")

