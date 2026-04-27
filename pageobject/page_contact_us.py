from selenium.webdriver.common.by import By
from pageobject.basepage import Common_Base_Page


class ContactUs(Common_Base_Page):

    # def __init__(self , driver):
    #     self.driver =  driver


    page_loaded_text = (By.XPATH , "//h2[normalize-space() = 'Get In Touch']")
    name = (By.NAME , "name")
    email = (By.NAME , "email")
    subject = (By.NAME , "subject")
    message = (By.ID, "message")
    upload_file = (By.NAME , "upload_file")
    submit_btn = (By.NAME, "submit")
    contact_us_submitted_msg = (By.XPATH , "//div[@class='status alert alert-success']")
    land_home = (By.XPATH , "//i[@class='fa fa-angle-double-left']")

    def contact_us_form(self , name , email , subject , message , upload_file):
        # fill the form
        self.send_keys_common_use(self.name , name)

        self.send_keys_common_use(self.email , email)

        self.send_keys_common_use(self.subject , subject)

        self.send_keys_common_use(self.message, message)

        self.send_keys_common_use(self.upload_file , upload_file)

        self.click_common_use(self.submit_btn)

    def is_successfully_submitted_contact_us_form(self):
        #Success! Your details have been submitted successfully.
        msg = self.driver.find_element(*self.contact_us_submitted_msg).text
        assert 'Success! Your details have' in msg

    def go_back_to_home_page_from_contact_us(self):
        self.click_common_use(self.land_home)
