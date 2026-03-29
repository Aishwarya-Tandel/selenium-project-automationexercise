from pageobject.common_base_page import Common_Base_Page
class Test_Login:
    def test_login(self,setup_teardown):
        driver =  setup_teardown

        #land on home page
        driver.get("https://automationexercise.com/")

        #click on login/signup menu
        #as it is from another folder/file/class so make object and use that method
        base = Common_Base_Page(driver)
        base.signup_login_menu()

