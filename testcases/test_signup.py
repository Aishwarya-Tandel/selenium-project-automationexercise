import json
import time
from pageobject.page_account_created import AccountCreated
import pytest
from pageobject.page_signup import SignUp
from pageobject.basepage import Common_Base_Page
from pageobject.page_login import Login
from utility.logging_log import Log_store
from utility.failed_screenshot import Screenshot_Capture

with open(r"C:\Users\LENOVO\PycharmProjects\selenium-project-automationexercise\testdata\signup_data.json") as f:
    li = json.load(f)
    data_list = li["signup"]

@pytest.mark.parametrize("data_name_email", data_list)
class TestSignUp:
    def test_signup(self,setup_teardown,data_name_email):
        driver = setup_teardown

        # log
        log = Log_store.get_log(__name__)

        driver.get("https://automationexercise.com/")

        base = Common_Base_Page(driver)
        base.signup_login_menu()

        signup_login = Login(driver)

        signup_login.signup_loginpage(data_name_email["name"] , data_name_email["email"])

        email_exist = signup_login.signuplogin_email_exists()
        if not email_exist:
            signup = SignUp(driver)
            signup.signup_with_mandatory_fields(data_name_email)

            act_created = AccountCreated(driver)
            msg = act_created.account_created()
            assert 'created' in msg.lower()
            log.debug(f"{msg}")
            log.debug("account created")

            act_created.continue_after_account_creation()
            log.debug("accounted created so continue.....")

            base.wait_for_clickable(base.logout) # wait till logout button clickable so no timeout

            log.debug("after account created, you continued and landed to home page")
        else:
            # not take screenshot of it
            Screenshot_Capture.failed_screenshot_capture(driver, "signup_email_exists")
            #valiadtion
            assert 'Email Address already exist!' in email_exist
            log.debug("as email already exist so no siign up with same email again")







