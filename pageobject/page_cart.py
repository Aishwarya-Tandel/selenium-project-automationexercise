from selenium.webdriver.common.by import By
from pageobject.basepage import Common_Base_Page


class Cart(Common_Base_Page):

    # def __init__(self , driver):
    #     self.driver = driver

    checkout_button = (By.XPATH,"//div/a[text()='Proceed To Checkout']")
    cart_empty = (By.XPATH, "//span/p/b[text()='Cart is empty!']")
    buy_product = (By.XPATH , "//p/a/u[text()='here']")
    remove_product = (By.XPATH , "//tr/td/a/i[@class='fa fa-times']")
    #if not logged in
    checkout_msg = (By.XPATH , "//div/h4[text()= 'Checkout']")
    button_register_login_on_checkout = (By.XPATH , "//p/a/u[normalize-space()='Register / Login']")
    button_continue_on_cart = (By.XPATH , "//div/button[text() = 'Continue On Cart']")

    def click_proceed_to_checkout(self):
        self.click_common_use(self.checkout_button)

    def click_continue_on_cart(self):
        self.click_common_use(self.button_continue_on_cart)

    def is_successfully_landed_on_same_page_after_click_on_continue_on_cart(self):
        msg = self.driver.find_element(self.checkout_msg).text
        assert 'view_cart' in self.driver.current_url

    def click_login_link_for_checkout(self):
        self.click_common_use(self.button_register_login_on_checkout)

    def is_successfully_landed_login_after_click_login_link_for_checkout(self):
        assert 'login' in self.driver.current_url

    def is_cart_empty(self):
        msg = self.driver.find_element(*self.cart_empty).text
        assert 'empty' in msg

    def validate_cart_empty(self):
        msg = self.driver.find_element(*self.cart_empty).text
        return msg

    def click_here_to_buy_product(self):
        self.click_common_use(self.buy_product)

    def is_successfully_click_on_here_to_buy_product(self):
        assert 'products' in self.driver.current_url






