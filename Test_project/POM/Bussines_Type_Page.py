from Lib import LIB
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class bussines_type_page:

    #---locators---
    bussines_type_dropdown               =(By.ID,'selected_industry')
    bussines_category                    = LIB.get_data("search_word")
    next_button                         = (By.CSS_SELECTOR, 'a.tw_button.dark_grey_bg.new_button.select_type')




    def __init__(self, browser):
        self.browser = browser

    #select bussines category
    def click_bussines_type_dropdown(self, browser):
        LIB.wait_for_element(self, browser, self.bussines_type_dropdown)
        select = Select(self.bussines_type_dropdown)
        select.select_by_visible_text(self.bussines_category)
    

    def click_next_button(self, browser):
        LIB.wait_for_element(self, browser, self.next_button)
        element = self.browser.find_element(*self.next_button)
        element.click()
    
