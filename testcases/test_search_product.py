import json
import time

import pytest
from pageobject.basepage import Common_Base_Page
from pageobject.home_page import HomePage
from pageobject.page_product_search import ProductSearch

with open(r"C:\Users\LENOVO\PycharmProjects\selenium-project-automationexercise\testdata\search_data.json") as f :
    data_list = json.load(f)
    data = [data_list[0]["search"][0]]

@pytest.mark.parametrize("data_use" , data)
class TestSearchProduct:
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

        p_names = search.product_names_and_click_on_view_product()
        assert 'Blue Top' in p_names

