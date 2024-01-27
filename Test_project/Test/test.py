from Lib import LIB
from POM.Home_Page import home_page
from POM.Bussines_Type_Page import bussines_type_page
from selenium import webdriver



def test():
        
    #open browser
    obj_lib = LIB()
    browser = obj_lib.open_browser()

    # navigate to url
    obj_lib.page_load(browser)

        
    obj_home_page = home_page(browser)
    obj_bussines_type_page = bussines_type_page(browser)

    #steps
    obj_home_page.click_radio_button()
    obj_bussines_type_page.click_bussines_type_dropdown()
    obj_bussines_type_page.click_next_button()

    obj_lib.close_browser()
            

