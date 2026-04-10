from selenium.webdriver.common.by import By
from pageobject.basepage import Common_Base_Page


class AccountCreated:
    def __init__(self,driver):
        self.driver =  driver

        self.common = Common_Base_Page(driver)

    #locators
    act = (By.XPATH,"//b[normalize-space()='Account Created!']")
    continue_button = (By.XPATH,"//div/a[normalize-space() = 'Continue']")


    def account_created(self):
        return self.driver.find_element(*self.act).text  #Account Created!    Congratulations! Your new account has been successfully created!

    def continue_after_account_creation(self):
        self.common.click_common_use(self.continue_button)