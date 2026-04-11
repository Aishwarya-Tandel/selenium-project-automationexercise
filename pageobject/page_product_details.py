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