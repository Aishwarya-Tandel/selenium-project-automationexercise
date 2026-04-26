from pageobject.page_cart import Cart
from pageobject.home_page import HomePage
from pageobject.page_login import Login


class TestCart:

    def test_cart_with_no_prelogin(self , setup_teardown):
        driver = setup_teardown

        # click on cart button from home page
        home = HomePage(driver)
        home.cart_menu()

        # if cart  is not empty --> then identify if not logged in ..... and if not logged in then process
        """ if not empty cart then
            find logout button... if not there means not logged in """

        # login = Login(driver)
        cart_obj = Cart(driver)

        # if not cart_obj.validate_cart_empty() and not login.login_success():

        if not cart_obj.validate_cart_empty():
            # click on proceed to checkout
            cart_obj.click_proceed_to_checkout()

            # if click on continue on cart-> stay on same page
            # if click on register/login button -> redirect to that page
            if cart_obj.click_continue_on_cart():
                cart_obj.is_successfully_landed_on_same_page_after_click_on_continue_on_cart()
            elif cart_obj.click_login_link_for_checkout():
                cart_obj.is_successfully_landed_login_after_click_login_link_for_checkout()
            else:
                print("user already logged in... we need to test non-login scenario")
        #cart is empty so click here to shopping
        else:
            cart_obj.is_cart_empty()
            cart_obj.click_here_to_buy_product()
            cart_obj.is_successfully_click_on_here_to_buy_product()




