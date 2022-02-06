from Pages.Base_page import BasePage
from Locators.Login_page_locators import LoginPageLocators as login_page_locators


class LoginPage(BasePage):
    def getting_current_url(self):
        current_url = self.browser.current_url
        return current_url

    def redirection_to_the_cart_page(self):
        cart_button = self.search_element(login_page_locators.CART_BUTTON)
        cart_button.click()

    def redirection_to_the_main_page(self):
        main_logo_button = self.search_element(login_page_locators.MAIN_LOGO_BUTTON)
        main_logo_button.click()

    def checking_cart(self):
        is_there_goods = self.search_element(login_page_locators.EMPTY_CART).text
        return is_there_goods
