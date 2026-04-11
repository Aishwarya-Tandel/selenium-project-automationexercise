import json
import pytest
from pageobject.basepage import Common_Base_Page
from pageobject.home_page import HomePage
from pageobject.page_product_search import ProductSearch

with open(r"C:\Users\LENOVO\PycharmProjects\selenium-project-automationexercise\testdata\search_data.json") as f :
    data_list = json.load(f)
    data = [data_list[0]["search"][0]]


class TestSearchProduct:
    @pytest.mark.parametrize("data_use", data)
    def test_search_product(self,setup_teardown , data_use):
        driver = setup_teardown

        #click on product menu
        home = HomePage(driver)
        home.products_menu()

        #type product name to search
        search = ProductSearch(driver)
        search.click_on_search_item(data_use)

        #click on search button
        search.click_on_search_button()

        #wait till search done
        base = Common_Base_Page(driver)
        base.wait_for_visibility(search.searched_done)

        assert 'searched' in search.is_searched_successful().lower()


    @pytest.mark.parametrize("already_searched_logic", data , indirect=True)
    def test_view_product(self,already_searched_logic):
        # driver = already_searched_logic

        #already loggedin prerequisite done so now view product whose name is "Blue Top"

        #as already object made for ProductSearch class and we returned it . we need same class
        # so instead of creating same class here we can just use same fixture or do # driver = already_searched_logic and use driver name


        # as with this method you already searched , on which product you want to click so click
        already_searched_logic.product_names_and_click_on_view_product()

        # check if successfully landed on product_details page
        already_searched_logic.is_successfully_reached_on_view_product()


