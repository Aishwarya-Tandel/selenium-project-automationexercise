from selenium.webdriver.common.by import By


class Common_Base_Page:
    def __init__(self,driver):
        self.driver = driver

    #home menu locator
    home= (By.XPATH,"//a[normalize-space()='Home']")
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
    # subscription locator
    subscription_email = (By.ID,"susbscribe_email")
    subscription_click = (By.ID,"subscribe")

    def home_menu(self):
        self.driver.find_element(*self.home).click()
    def products_menu(self):
        self.driver.find_element(*self.products).click()
    def cart_menu(self):
        self.driver.find_element(*self.cart).click()
    def signup_login_menu(self):
        self.driver.find_element(*self.signup_login).click()
    def test_menu(self):
        self.driver.find_element(*self.test).click()
    def contact_menu(self):
        self.driver.find_element(*self.contact).click()
    def subscription(self,email):
        self.driver.find_element(*self.subscription_email).send_keys(email)
        self.driver.find_element(*self.subscription_click).click()


