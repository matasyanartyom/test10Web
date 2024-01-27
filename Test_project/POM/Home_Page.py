from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from Lib import LIB


class home_page:

    #---locators---
    inf_website_button   = (By.ID, 'website_type_default')
    next_button          = (By.CSS_SELECTOR, 'a.tw_button.dark_grey_bg.new_button.select_type')




    #---methods---
    def __init__(self, browser):
        self.browser = browser

    #click on radio button
    def click_radio_button(self, browser):
        LIB.wait_for_element(self, browser, self.inf_website_button)
        element = self.browser.find_element(*self.inf_website_button)
        element.click()


    #click on next button
    def click_next_button(self, browser):
        LIB.wait_for_element(self, browser, self.next_button)
        element = self.browser.find_element(*self.next_button)
        element.click()

        
   
