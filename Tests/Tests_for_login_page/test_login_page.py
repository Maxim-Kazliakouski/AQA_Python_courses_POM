from Pages.Login_page import LoginPage
from Tests.Tests_for_login_page.data_login_page import TestData
import time


class Test_for_login_page:
    class Test_positive:
        def test_user_on_login_page(self, browser):
            """
            This case checks, that user gets to the login page
            """
            link = TestData.LOGIN_URL
            page = LoginPage(browser, link)
            page.open_page(TestData.LOGIN_URL)
            login_page = page.getting_current_url()
            time.sleep(2)
            assert login_page == TestData.LOGIN_URL, "User isn't on login page"

        def test_redirection_from_login_to_cart_page(self, browser):
            """
            This case checks, that user after clicking on 'Cart' button
            redirects to teh Cart page from login page
            """
            link = TestData.LOGIN_URL
            page = LoginPage(browser, link)
            page.open_page(TestData.LOGIN_URL)
            page.redirection_to_the_cart_page()
            time.sleep(2)
            cart_page = page.getting_current_url()
            assert cart_page == TestData.CART_PAGE_URL, "User isn't on cart page"

        def test_checking_empty_cart(self, browser):
            """
            This case checks, that that cart is empty, if user redirects to the cart page
            from login page without any orders
            """
            link = TestData.LOGIN_URL
            page = LoginPage(browser, link)
            page.open_page(TestData.LOGIN_URL)
            page.redirection_to_the_cart_page()
            checking_cart = page.checking_cart()
            assert checking_cart == TestData.EMPTY_CART, "The cart isn't empty"

        def test_redirection_from_login_to_main_page(self, browser):
            """
            This case checks, that user after clicking on 'Main logo'
            button redirects to the main page
            """
            link = TestData.LOGIN_URL
            page = LoginPage(browser, link)
            page.open_page(TestData.LOGIN_URL)
            page.redirection_to_the_main_page()
            main_page = page.getting_current_url()
            assert main_page == TestData.MAIN_PAGE_URL, "User isn't on main page"

