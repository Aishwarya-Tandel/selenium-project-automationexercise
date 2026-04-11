from selenium.webdriver.common.by import By
from pageobject.basepage import Common_Base_Page


class ProductSearch(Common_Base_Page):

    # no need as Common_Base_Page already have it so need double/duplicate
    # def __init__(self,driver):
    #     self.driver = driver

    #locators
    search_product = (By.ID, "search_product")
    search_button = (By.XPATH, "//button[@id='submit_search']")
    searched_done = (By.XPATH,"//h2[normalize-space()='Searched Products']")

    women_products = (By.XPATH, "//h4/a[@href='#Women']")
    dress = (By.XPATH, "//ul/li/a[@href='/category_products/1']")
    tops = (By.XPATH,"//ul/li/a[@href='/category_products/2']")
    sarees = (By.XPATH,"//ul/li/a[@href='/category_products/7']")

    men_products = (By.XPATH,"//h4/a[@href='#Men']")
    tshirts = (By.XPATH, "//ul/li/a[@href='/category_products/3']")
    jeans = (By.XPATH, "//ul/li/a[@href='/category_products/6']")

    kids_product = (By.XPATH,"//h4/a[@href='#Kids']")

    p_names = (By.XPATH,"//div[@class='productinfo text-center']/p")
    #specific product locator to use to click on view product
    # till he same then continues --> //div[@class='productinfo text-center']/p[normalize-space()='Summer White Top']
    view_product_button = (By.XPATH, ".//ancestor::div[@class='product-image-wrapper']/div[@class='choose']/ul/li/a[normalize-space()='View Product']")

    brand_polo = (By.LINK_TEXT,"/brand_products/Polo")
    brand_H_and_M = (By.LINK_TEXT, "/brand_products/H&M")
    brand_mademe = (By.LINK_TEXT, "/brand_products/Madame")
    brand_mast_and_harbour = (By.LINK_TEXT, "/brand_products/Mast & Harbour")
    brand_babyhug = (By.LINK_TEXT, "/brand_products/Babyhug")
    brand_allen_solly_junior = (By.LINK_TEXT, "/brand_products/Allen Solly Junior")
    brand_kookie_kids = (By.LINK_TEXT, "/brand_products/Kookie Kids")
    brand_biba = (By.LINK_TEXT, "/brand_products/Biba")



    def click_on_search_item(self,type_search):
        self.send_keys_common_use(self.search_product , type_search)

    def click_on_search_button(self):
        self.click_common_use(self.search_button)

    def is_searched_successful(self):
        return self.driver.find_element(*self.searched_done).text

    def product_names_and_click_on_view_product(self):
        names = self.driver.find_elements(*self.p_names)
        # all_products_names_list = []
        for name in names:
            # all_products_names_list.append(name.text)

            if name.text == 'Summer White Top':
                #click on that specific view product
                p = name.find_element(*self.view_product_button).click()
                break


    def is_successfully_reached_on_view_product(self):
        assert 'product_details' in self.driver.current_url

    def click_on_women_products(self):
        self.click_common_use(self.women_products)

    def click_on_women_dress_products(self):
        self.click_common_use(self.dress)

    def click_on_women_tops_products(self):
        self.click_common_use(self.tops)

    def click_on_women_sarees_products(self):
        self.click_common_use(self.sarees)

    def click_on_men_products(self):
        self.click_common_use(self.men_products)

    def click_on_men_tshirts_products(self):
        self.click_common_use(self.tshirts)

    def click_on_men_jeans_products(self):
        self.click_common_use(self.jeans)

    def click_on_kids_products(self):
        self.click_common_use(self.kids_product)

    def click_on_brand_polo(self):
        self.click_common_use(self.brand_polo)

    def click_on_brand_h_and_m(self):
        self.click_common_use(self.brand_H_and_M)

    def click_on_brand_mademe(self):
        self.click_common_use(self.brand_mademe)

    def click_on_brand_mast_and_harbour(self):
        self.click_common_use(self.brand_mast_and_harbour)

    def click_on_brand_babyhug(self):
        self.click_common_use(self.brand_babyhug)

    def click_on_brand_allen_solly_junior(self):
        self.click_common_use(self.brand_allen_solly_junior)

    def click_on_brand_kookie_kids(self):
        self.click_common_use(self.brand_kookie_kids)

    def click_on_brand_biba(self):
        self.click_common_use(self.brand_biba)
