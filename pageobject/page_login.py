from selenium.webdriver.common.by import By
from utility.logging_log import Log_store
from pageobject.basepage import Common_Base_Page


class Login:

    def __init__(self,driver):
        self.driver = driver

        self.common = Common_Base_Page(self.driver)

    ##logger call
    log = Log_store.get_log(__name__)

    #locators for login
    login_email = (By.XPATH, "//input[@data-qa='login-email']")
    login_password = (By.XPATH, "//input[@data-qa='login-password']")
    login_button = (By.XPATH, "//button[@data-qa='login-button']")
    #Login fail
    msg = (By.XPATH,"//p[text()='Your email or password is incorrect!']")
    #locators for signup in login page
    signup_name = (By.XPATH, "//input[@data-qa='signup-name']")
    signup_email = (By.XPATH, "//input[@data-qa='signup-email']")
    signup_button = (By.XPATH, "//button[@data-qa='signup-button']")
    msg = (By.XPATH,"//p[text()='Email Address already exist!']")

    def login(self,email,password):
        self.driver.find_element(*self.login_email).send_keys(email)
        self.driver.find_element(*self.login_password).send_keys(password)
        #was giving "error":"element click intercepted" , may be some ads were overlapping or something was blocking
        #so do wait untile it's ready to click
        self.common.wait_for_clickable(self.login_button).click()
        # self.driver.find_element(*self.login_button).click()

        self.log.debug("logging in")


    def login_error_message(self):
        message = self.driver.find_element(*self.msg).text
        return message

    def login_success(self):
        # put one wait condition , like as you know if logout menu comes means successfull login...
        #so lets wait till logot menu visible/clickable
        #use same wait method from common page and logout element method also from common page

        self.common.wait_for_clickable(self.common.logout)
        self.log.debug("successfully logged in")
        return True


    def signup_loginpage(self,name,email):
        self.driver.find_element(*self.signup_name).send_keys(name)
        self.driver.find_element(*self.signup_email).send_keys(email)
        self.driver.find_element(*self.signup_button).click()
        self.log.debug("signing in")

    def signuplogin_email_exists(self):
            # as this element you will only found when emil already exist message shows
            # if new email then it will try to search for that text but not there so NoSuchElement will occur
            #so return msg only when there else return None
            try:
                return self.driver.find_element(*self.msg).text
            except:
                return None

