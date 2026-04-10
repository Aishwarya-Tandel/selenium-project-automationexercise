from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class Common_Base_Page:
    def __init__(self,driver):
        self.driver = driver

    #wait till element clickable logic
    def wait_for_clickable(self,by_locator):
        wait  = WebDriverWait(self.driver,15)
        return wait.until(expected_conditions.element_to_be_clickable(by_locator))

    #wait till element visible logic
    def wait_for_visibility(self,by_locator):
        wait  = WebDriverWait(self.driver,15)
        return wait.until(expected_conditions.visibility_of_element_located(by_locator))

    # scroll down till element
    def scroll_down(self,element):
        action = ActionChains()
        return action.move_to_element(element)

    #static dropdwn
    def static_dropdown(self,element,val):
        select = Select(element)
        return select.select_by_value(val)

    # click()
    def click_common_use(self,locator):
        self.driver.find_element(*locator).click()

    def send_keys_common_use(self,locator,input_val):
        self.driver.find_element(*locator).send_keys(input_val)


