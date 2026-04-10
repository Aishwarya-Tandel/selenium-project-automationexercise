from selenium.webdriver.common.by import By

from pageobject.basepage import Common_Base_Page


class HomePage(Common_Base_Page):
    # def __init__(self,driver):
    #     super().__init__(driver)
    #     self.driver = driver

    # no need above 3 line because no need to cretae init method twise here 1 for HomePge and 1 for Common_Base_Page using super()
    # because when you will inherit , with Common_Base_Page CLASS , init() is any way coming and both init__ do same here... there is no additional details this or that init__ have so no need to write

    #home menu locator
    home_m= (By.XPATH,"//a[normalize-space()='Home']")
    #Products Menu Locator
    products = (By.XPATH,"//li/a[@href='/products']")
    #CART MENU LOCATOR
    cart = (By.LINK_TEXT,"Cart")
    #SIGNUP/LOGIN MENU Locator
    signup_login = (By.LINK_TEXT, "Signup / Login")
    #test menu locator
    test = (By.LINK_TEXT, "Test Cases")
    #contact menu locator
    contact = (By.LINK_TEXT, "Contact us")
    #logout menu locator
    logout = (By.XPATH,"//a[@href='/logout']")
    # subscription locator
    subscription_email = (By.ID,"susbscribe_email")
    subscription_click = (By.ID,"subscribe")

    def home_menu(self):
        self.click_common_use(self.home_m)
    def products_menu(self):
        self.click_common_use(self.products)
    def cart_menu(self):
        self.click_common_use(self.cart)
    def signup_login_menu(self):
        self.wait_for_clickable(self.signup_login).click()
        # self.driver.find_element(*self.signup_login).click()
    def test_menu(self):
        self.click_common_use(self.test)
    def contact_menu(self):
        self.click_common_use(self.contact)

    def logout_menu(self):
        self.wait_for_clickable(self.logout).click()
        # self.click_common_use(self.logout) or # self.driver.find_element(*self.logout).click()

    def is_successfully_logged_out(self):
        return 'login' in self.driver.current_url     # when you click on logout button in url it will redirect to login page so you will see 'login' keyword in URL so with you can assert in test so return that

    def subscription(self,email):
        self.send_keys_common_use(self.subscription_email , email)
        self.click_common_use(self.subscription_click)