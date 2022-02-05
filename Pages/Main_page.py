import time
from selenium.webdriver.common.by import By
import sys
from Pages.Base_page import BasePage
from Locators.Main_page_locators import MainPageLocators as main_page_locators
from Tests.Tests_for_main_page.data_main_page import TestData
sys.path.insert(0, '/Volumes/Work/Python_courses/Project/POM')


class MainPage(BasePage):
    def getting_current_url(self):
        # BasePage.open_page(self, TestData.MAIN_PAGE_URL)
        current_url = self.browser.current_url
        return current_url

    def redirection_to_the_cart_page(self):
        cart_button = self.browser.find_element(*main_page_locators.CART_BUTTON)
        cart_button.click()

    def redirection_to_the_login_page(self):
        login_button = self.browser.find_element(*main_page_locators.LOGIN_BUTTON)
        login_button.click()

    def checking_cart(self):
        is_there_goods = self.browser.find_element(*main_page_locators.EMPTY_CART).text
        return is_there_goods

