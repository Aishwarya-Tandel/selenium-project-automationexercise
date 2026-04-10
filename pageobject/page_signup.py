from selenium.webdriver.common.by import By
from pageobject.basepage import Common_Base_Page
from utility.logging_log import Log_store


class SignUp:

    def __init__(self,driver):
        self.driver =  driver

        self.common = Common_Base_Page(self.driver)

    #log
    log = Log_store.get_log(__name__)

    #locators for signup/account information
    title = (By.XPATH,"//label[normalize-space()='Mr.']")
    password = (By.CSS_SELECTOR,"#password")
    day = (By.CSS_SELECTOR,"#uniform-days")
    month = (By.CSS_SELECTOR,"#months")
    year = (By.CSS_SELECTOR, "#years")
    checkbox = (By.XPATH,"//label[normalize-space()='Sign up for our newsletter!']")
    # locators for signup/address information
    first_name = (By.ID,"first_name")
    last_name = (By.ID,"last_name")
    company = (By.ID,"company")
    address1 = (By.ID,"address1")
    address2 = (By.ID, "address2")
    country = (By.ID,"country")
    state = (By.ID,"state")
    city = (By.ID, "city")
    zipcode = (By.ID, "zipcode")
    mobile_number = (By.ID, "mobile_number")
    create_account_button = (By.XPATH,"//button[normalize-space()='Create Account']")

    # wait locator
    wait_ele = (By.XPATH,"//b[normalize-space()='Enter Account Information']")

    def signup_with_mandatory_fields(self,data):
        #note : you can pass all 9 parameter here and when calling in test method, there also you have to pass value for all 9 (using parametrize or hardcodedc but harded not reffere)
        # so instead of passing this all 9 here (f_name,l_name,company_detail,address1_detail,country_detail,state_detail,citi_detail,zipcode_detail,mobile_detail) ,
        #  just pass 1 variable and use variable["key"] . example : data["f_name]
        # same we were going to pass in test also right,  but it will be complex as when we cann this method in test, we have to pass all 9 there and sa this method we are using in next method also so 9+5 = 14 so it will be little looks complex.....
        # like in test file, for example data is a variable where parametrize value so there also we can write like data["f_name"]
        # but just to avoid length, instead of --> def signup_with_mandatory_fields(self,f_name,l_name,company_detail,address1_detail,country_detail,state_detail,citi_detail,zipcode_detail,mobile_detail): , we are writtimg above

        #wait for page to load and see if element visible then starts
        self.common.wait_for_visibility(self.wait_ele)

        #password enter
        self.common.send_keys_common_use(self.password , data["password"])
        #first name
        self.common.send_keys_common_use(self.first_name , data["f_name"])
        #lastname
        self.common.send_keys_common_use(self.last_name , data["l_name"])
        #company
        self.common.send_keys_common_use(self.company , data["company_detail"])
        #address1
        self.common.send_keys_common_use(self.address1 , data["address1_detail"])
        #country
        self.common.send_keys_common_use(self.country , data["country_detail"])
        #state
        self.common.send_keys_common_use(self.state , data["state_detail"])
        #citi
        self.common.send_keys_common_use(self.city , data["citi_detail"])
        #zipcode
        self.common.send_keys_common_use(self.zipcode , data["zipcode_detail"])
        #mobileno
        self.common.send_keys_common_use(self.mobile_number , data["mobile_detail"])

        #click create account button
        self.common.click_common_use(self.create_account_button)

    def signup_with_all_fields(self,data):
        #note : instead of def signup_with_all_fields(self,day_val,month_val ,year_vale ,address2_detail,f_name,l_name,company_detail,address1_detail,country_detail,state_detail,citi_detail,zipcode_detail,mobile_detail), write like above
        #signup_with_mandatory_fields(so use that func here) + other remaining

        self.signup_with_mandatory_fields(data) #expect same parameter and pass same in this signup_will_all_fields() as well so total 9+4 . so instead of self.signup_with_mandatory_fields(f_name,l_name,company_detail,address1_detail,country_detail,state_detail,citi_detail,zipcode_detail,mobile_detail) , write like above

        #title
        self.common.click_common_use(self.title)

        # select  date_of_birth
        day_click = self.driver.find_element(*self.day)  # for static dropdown no need to click(), we used select_by_value() which will take carte
        self.common.static_dropdown(day_click,data["day_val"])  # here val(variable we passed in static_method)=day_val so ideally val=10 I want to sleected but don;t pass hard coded value here, directly use in test method, there you can pass harcoded but still use parametrize for this value

        month_click = self.driver.find_element(*self.month)
        self.common.static_dropdown(month_click, data["month_val"])

        year_click = self.driver.find_element(*self.year)
        self.common.static_dropdown(year_click, data["year_vale"])

        #checkbox
        self.common.click_common_use(self.checkbox)
        #address2
        self.common.send_keys_common_use(self.address2 , data["address2_detail"])

        #click create account
        self.common.click_common_use(self.create_account_button)


