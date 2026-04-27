import pytest

from pageobject.page_contact_us import ContactUs
from pageobject.home_page import HomePage
from utility.read_conig_ini_file import ReadConfig
from utility.read_contact_us_form_data import ReadContactUsFormData

data = ReadContactUsFormData.read_contact_us_form_data()

@pytest.mark.parametrize("name,email,subject,message" , data)
class TestContactUs:
    def test_contact_us(self,setup_teardown , name,email,subject,message):
        driver = setup_teardown

        #Click on contact us page after landing on home page
        home = HomePage(driver)
        home.contact_menu()

        # check if successfully landed on contact us page
        assert 'contact_us' in driver.current_url

        contact = ContactUs(driver)
        path = ReadConfig.get_file_upload_path()
        contact.contact_us_form(name,email,subject,message, path)

        # after submit form 1 alert come so click on OK
        alt = driver.switch_to.alert
        alt.accept()

        # check if submitted successfully
        contact.is_successfully_submitted_contact_us_form()

        # go back to home page
        contact.go_back_to_home_page_from_contact_us()
