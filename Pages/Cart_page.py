from Pages.Base_page import BasePage
from Locators.Cart_page_locators import CartPageLocators as cart_page_locators


class CartPage(BasePage):
    def getting_current_url(self):
        current_url = self.browser.current_url
        return current_url

    def redirection_to_the_login_page(self):
        login_button = self.search_element(cart_page_locators.LOGIN_BUTTON)
        login_button.click()

    def redirection_to_the_main_page(self):
        main_logo_button = self.search_element(cart_page_locators.MAIN_LOGO_BUTTON)
        main_logo_button.click()

    def checking_cart(self):
        is_there_goods = self.search_element(cart_page_locators.EMPTY_CART).text
        return is_there_goods
