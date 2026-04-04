from selenium.webdriver.common.by import By


class AccountCreated:
    def __init__(self,driver):
        self.driver =  driver

    #locators
    act = (By.XPATH,"//b[normalize-space()='Account Created!']")
    continue_button = (By.XPATH,"//div/a[normalize-space() = 'Continue']")

    def account_created(self):
        return self.driver.find_element(*self.act).text  #Account Created!    Congratulations! Your new account has been successfully created!

    def continue_after_account_creation(self):
        self.driver.find_element(*self.continue_button).click()