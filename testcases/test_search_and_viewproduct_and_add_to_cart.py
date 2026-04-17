import json
import pytest
from pageobject.basepage import Common_Base_Page
from pageobject.home_page import HomePage
from pageobject.page_product_search import ProductSearch
from pageobject.page_product_details import ProductDetails

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
        driver , search = already_searched_logic # return driver and "ProductSearch" class object

        #already loggedin prerequisite done so now view product whose name is "Blue Top"

        #as already object made for ProductSearch class and we returned it . we need same class
        # so instead of creating same class here we can just use same fixture or do # driver = already_searched_logic and use driver name


        # as with this method you already searched , on which product you want to click so click
        search.product_names_and_click_on_view_product()

        # check if successfully landed on product_details page
        search.is_successfully_reached_on_view_product()

    @pytest.mark.parametrize("already_searched_logic", data, indirect=True)
    def test_add_to_cart_and_view_product_on_product_search_page(self,already_searched_logic):
        driver , search = already_searched_logic # return driver and "ProductSearch" class object

        #already logged in prerequisite done so now view product whose name is "Blue Top"

        #as already object made for ProductSearch class and we returned it . we need same class
        # so instead of creating same class here we can just use same fixture or do # driver = already_searched_logic and use driver name

        """ I have already created "add to card" function in "ProductDetails" class , 
        same button on ProductSearch page as well.
        but locators different so create that locator for that page
        """
        search.click_on_add_to_cart_from_product_search()

        """
            as we saw on ProductDetails Page --> add to cart + view cart or continue shopping
            for add to cart button differnt locators so we created seperate method
            But after click on "add to cart" --> the popup come for view cart and continue shopping
            which have same locators on ProductSearch Page as well 
            so instead creating different method lets use same
            
            also to validate add to cart success or not also we have method in ProductDeatils so use same

        """
        # as we have to use ProductDetails page class but we are not returning that from fixture
        # so let's create one
        product = ProductDetails(driver)

        # check successfully added to cart from product search page
        product.is_add_to_cart_successful()

        # so click on view cart, land to respective page
        product.click_on_view_cart()
        #check if successfully landed to view page
        product.is_landed_on_view_cart_successfully()



    @pytest.mark.parametrize("already_searched_logic", data, indirect=True)
    def test_add_to_cart_and_continue_shopping_on_product_search_page(self , already_searched_logic):
        driver, search = already_searched_logic  # return driver and "ProductSearch" class object

        # already loggedin prerequisite done so now view product whose name is "Blue Top"

        # as already object made for ProductSearch class and we returned it . we need same class
        # so instead of creating same class here we can just use same fixture or do # driver = already_searched_logic and use driver name

        """ I have already created "add to card" function in "ProductDetails" class , 
        same button on ProductSearch page as well.
        but locators different so create that locator for that page
        """
        search.click_on_add_to_cart_from_product_search()

        """
            as we saw on ProductDetails Page --> add to cart + view cart or continue shopping
            for add to cart button differnt locators so we created seperate method
            But after click on "add to cart" --> the popup come for view cart and continue shopping
            which have same locators on ProductSearch Page as well 
            so instead creating different method lets use same
    
            also to validate add to cart success or not also we have method in ProductDeatils so use same
    
        """
        # as we have to use ProductDetails page class but we are not returning that from fixture
        # so let's create one
        product = ProductDetails(driver)

        # check successfully added to cart from product search page
        product.is_add_to_cart_successful()

        # click on continue shopping
        product.continue_shopping()
