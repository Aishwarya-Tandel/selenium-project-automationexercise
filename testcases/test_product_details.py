import json
import time
import pytest
from pageobject.page_product_details import ProductDetails


with open(r"C:\Users\LENOVO\PycharmProjects\selenium-project-automationexercise\testdata\search_data.json") as f :
    data_list = json.load(f)
    data = [data_list[0]["search"][0]]

class TestProductDetails:
    @pytest.mark.parametrize("already_searched_logic" , data, indirect=True)
    def test_submit_review_of_product(self,already_searched_logic):
        driver , search = already_searched_logic  # this line mandatory when returning multiple values so use variable accordingly
        #you should be at product details page
        # fixture "already_searched_logic" already have setup_teardown fixture so ne need to add that fixture again
        # fixture "already_searched_logic" will do till search

        # now click on view product
        search.product_names_and_click_on_view_product() #so instead this use search variable : already_searched_logic.product_names_and_click_on_view_product()

        #check successfully landed to product details page after clicked on view product
        search.is_successfully_reached_on_view_product() # so instead this use search variable : already_searched_logic.is_successfully_reached_on_view_product()

        #now fill and submit form
        review_d = ProductDetails(driver)
        review_d.write_and_submit_review("a","a@d.com","good")

        # check if review submitted successfully
        msg = review_d.is_review_submitted_successfully()

        assert 'Thank you' in msg     # Thank you for your review.
        print(msg)