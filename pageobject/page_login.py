from selenium.webdriver.common.by import By

from pageobject.home_page import HomePage
from utility.logging_log import Log_store
from pageobject.basepage import Common_Base_Page


class Login:

    def __init__(self,driver):
        self.driver = driver

        # we can use inheritence but in POM avoid
        # so either like this so either 1 class use as inheritance or follow this
        self.common = Common_Base_Page(self.driver)
        self.homepage = HomePage(self.driver)

    ##logger call
    log = Log_store.get_log(__name__)

    #locators for login
    login_email = (By.XPATH, "//input[@data-qa='login-email']")
    login_password = (By.XPATH, "//input[@data-qa='login-password']")
    login_button = (By.XPATH, "//button[@data-qa='login-button']")
    #Login fail
    msg_login = (By.XPATH,"//p[normalize-space()='Your email or password is incorrect!']")
    #locators for signup in login page
    signup_name = (By.XPATH, "//input[@data-qa='signup-name']")
    signup_email = (By.XPATH, "//input[@data-qa='signup-email']")
    signup_button = (By.XPATH, "//button[@data-qa='signup-button']")
    msg_signup_exists = (By.XPATH,"//p[normalize-space()='Email Address already exist!']")

    def login(self,email,password):
        self.common.send_keys_common_use(self.login_email , email)
        self.common.send_keys_common_use(self.login_password , password)
        #was giving "error":"element click intercepted" , may be some ads were overlapping or something was blocking
        #so do wait untile it's ready to click
        self.common.wait_for_clickable(self.login_button).click()
        # self.driver.find_element(*self.login_button).click()

        self.log.debug("logging in")


    def login_error_message(self):
        message = self.driver.find_element(*self.msg_login).text
        return message

    def login_success(self):
        # put one wait condition , like as you know if logout menu comes means successful login...
        #so lets wait till logot menu visible/clickable
        #use same wait method from common page and logout element method  from home page

        self.common.wait_for_clickable(self.homepage.logout)
        self.log.debug("successfully logged in")
        return True


    def signup_loginpage(self,name,email):
        self.common.send_keys_common_use(self.signup_name , name)
        self.common.send_keys_common_use(self.signup_email , email)
        self.common.click_common_use(self.signup_button)
        self.log.debug("signing in")

    def signuplogin_email_exists(self):
        # as this element you will only found when emil already exist message shows
        # if new email then it will try to search for that text but not there so NoSuchElement will occur
        #so return msg only when there else return None
        try:
            return self.driver.find_element(*self.msg_signup_exists).text
        except:
            return None

