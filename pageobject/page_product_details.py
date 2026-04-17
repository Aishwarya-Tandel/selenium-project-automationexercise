from selenium.webdriver.common.by import By
from pageobject.basepage import Common_Base_Page


class ProductDetails(Common_Base_Page):
    # def __init__(self,driver):
    #     self.driver = driver

    #locators to write review
    name = (By.ID,"name")
    email = (By.ID,"email")
    review = (By.ID,"review")
    review_submit_button = (By.ID,"button-review")
    review_submitted_message = (By.XPATH,"//div[@class='alert-success alert']/span[normalize-space()='Thank you for your review.']")
    cart_button = (By.XPATH,"//div/span/button[normalize-space()='Add to cart']")
    card_success =(By.XPATH, "//div/p[normalize-space()='Your product has been added to cart.']")
    shop = (By.XPATH , "//div/button[normalize-space()='Continue Shopping']")
    v_cart = (By.XPATH , "//div/p/a/u[text()='View Cart']")

    def product_details(self):
        pass

    def write_and_submit_review(self,name , email , review):
        self.send_keys_common_use(self.name,name)
        self.send_keys_common_use(self.email, email)
        self.send_keys_common_use(self.review, review)
        self.click_common_use(self.review_submit_button)

    def is_review_submitted_successfully(self):
        w = self.wait_for_visibility(self.review_submitted_message)
        return w.text

    def click_on_add_to_cart(self):
        self.click_common_use(self.cart_button)

    def is_add_to_cart_successful(self):
        m = self.wait_for_visibility(self.card_success).text
        assert 'product has been added' in m

    def continue_shopping(self):
        self.click_common_use(self.shop)

    def click_on_view_cart(self):
        self.click_common_use(self.v_cart)

    def is_landed_on_view_cart_successfully(self):
        assert 'view_cart' in self.driver.current_url