# pre-requisite -  reached at product details

import json
import time
import pytest
from pageobject.page_product_details import ProductDetails


with open(r"C:\Users\LENOVO\PycharmProjects\selenium-project-automationexercise\testdata\search_data.json") as f :
    data_list = json.load(f)
    data = [data_list[0]["search"][0]]

@pytest.mark.parametrize("already_searched_logic", data, indirect=True)
class TestProductDetails:

    def test_submit_review_of_product(self,already_reached_product_details_page_logic):
        product , search = already_reached_product_details_page_logic  # if only return 1 value then instead of storing in other variable, you can directly also use fixture name
        #you should be at product details page
        # fixture "already_reached_product_details_page_logic" already have setup_teardown fixture so no need to add that fixture again
        # fixture "already_reached_product_details_page_logic" will do till reach on view product successfully

        #now fill and submit form
        # product = ProductDetails(driver) - no need
        product.write_and_submit_review("a","a@d.com","good")

        # check if review submitted successfully
        msg = product.is_review_submitted_successfully()

        assert 'Thank you' in msg     # Thank you for your review.
        print(msg)

    #no parametrize needs as we are not sending any data to fixture so normal use like we do for setup_teardown
    def test_add_to_cart_and_continue_shopping_in_product_details_page(self , already_reached_product_details_page_logic):
        product , search = already_reached_product_details_page_logic  # if only return 1 value then instead of storing in other variable, you can directly also use fixture name

        #now click on "add to cart"
        # review_d = ProductDetails(driver) - no need
        product.click_on_add_to_cart()

        product.is_add_to_cart_successful()

        # now continue shopping
        product.continue_shopping()


    #no parametrize needs as we are not sending any data to fixture so normal use like we do for setup_teardown
    def test_add_to_cart_and_view_cart_in_product_details_page(self , already_reached_product_details_page_logic):
        product , search = already_reached_product_details_page_logic  # if only return 1 value then instead of storing in other variable, you can directly also use fixture name

        #now click on "add to cart"
        # review_d = ProductDetails(driver)  - no need
        product.click_on_add_to_cart()

        product.is_add_to_cart_successful()

        #now click on view Cart
        product.click_on_view_cart()

        # check if successfully landed on view cart page
        product.is_landed_on_view_cart_successfully()






