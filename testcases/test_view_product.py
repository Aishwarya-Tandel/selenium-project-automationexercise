#pre-requisite --> search product first
import json
import time

import pytest

with open(r"C:\Users\LENOVO\PycharmProjects\selenium-project-automationexercise\testdata\search_data.json") as f :
    data_list = json.load(f)
    data = [data_list[0]["search"][0]]

class TestViewProduct:
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

        time.sleep(5)
