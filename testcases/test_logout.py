import pytest
import json
# from pageobject.home_page import HomePage
from pageobject.basepage import Common_Base_Page

with open(r"C:\Users\LENOVO\PycharmProjects\selenium-project-automationexercise\testdata\login_data.json") as f:
    data_j = json.load(f)


class TestLogout:
    @pytest.mark.parametrize("logged_in_user", [data_j[0]], indirect=True)
    def test_logout(self ,logged_in_user): # here no need to write "setup_teardown" fixture because this fixture "logged_in_user", already have this setup_teardown

        # covered in fixture
        #trigger landing page
        # driver = logged_in_user
        # driver.get("https://automationexercise.com/")

        """
        #once successfully login then only you can log out
        #no need to write code again of login to duplicate it.
        #use page plus fixture(pre-requisite logic) and use same logic
        you passed fixture 'logged_in_user' , which is logic for successful login
        so you logged in now

        #now do log out but no need to create HomePage object to call logout()
         because we already created that object in same fixture
         so just call logout() with same fixture
        """
        # home = HomePage(driver)
        # home.logout()

        logged_in_user.logout_menu()

        #now check if successfully logged out
        assert logged_in_user.is_successfully_logged_out
