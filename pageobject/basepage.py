from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


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
    #logout menu locator
    logout = (By.XPATH,"//a[@href='/logout']")
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
        self.wait_for_clickable(self.signup_login).click()
        # self.driver.find_element(*self.signup_login).click()
    def test_menu(self):
        self.driver.find_element(*self.test).click()
    def contact_menu(self):
        self.driver.find_element(*self.contact).click()

    def logout_menu(self):
        self.driver.find_element(*self.logout).click()

    def subscription(self,email):
        self.driver.find_element(*self.subscription_email).send_keys(email)
        self.driver.find_element(*self.subscription_click).click()

    #wait till element clickable logic
    def wait_for_clickable(self,by_locator):
        wait  = WebDriverWait(self.driver,15)
        return wait.until(expected_conditions.element_to_be_clickable(by_locator))

    #wait till element visible logic
    def wait_for_visibility(self,by_locator):
        wait  = WebDriverWait(self.driver,15)
        return wait.until(expected_conditions.visibility_of_element_located(by_locator))

    # scroll down till element
    def scroll_down(self,element):
        action = ActionChains()
        return action.move_to_element(element)

    #static dropdwn
    def static_dropdown(self,element,val):
        select = Select(element)
        return select.select_by_value(val)


