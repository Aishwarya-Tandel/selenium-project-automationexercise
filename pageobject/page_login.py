from selenium.webdriver.common.by import By


class Login:

    def __init__(self,driver):
        self.driver = driver

    #locators for login
    login_email = (By.XPATH, "//input[@data-qa='login-email']")
    login_password = (By.XPATH, "//input[@data-qa='login-password']")
    login_button = (By.XPATH, "//button[@data-qa='login-button']")
    #locators for signup
    signup_name = (By.XPATH, "//input[@data-qa='signup-name']")
    signup_email = (By.XPATH, "//input[@data-qa='signup-email']")
    signup_button = (By.XPATH, "//button[@data-qa='signup-button']")

    def login(self,email,password):
        self.driver.find_element(*self.login_email).send_keys(email)
        self.driver.find_element(*self.login_password).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def signup_loginpage(self,name,email):
        self.driver.find_element(*self.signup_name).send_keys(name)
        self.driver.find_element(*self.signup_email).send_keys(email)
        self.driver.find_element(*self.signup_button).click()
