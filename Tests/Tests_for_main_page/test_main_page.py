from Tests.Tests_for_main_page.data_main_page import TestData
from Pages.Main_page import MainPage
import time


class Test_for_main_page:
    class Test_positive:
        def test_user_on_main_page(self, browser):
            """
            This case checks, that user gets to the main page
            """
            link = TestData.MAIN_PAGE_URL
            page = MainPage(browser, link)
            page.open_page(TestData.MAIN_PAGE_URL)
            main_page = page.getting_current_url()
            assert main_page == TestData.MAIN_PAGE_URL, 'User is not on main page'

        def test_redirection_from_main_to_cart_page(self, browser):
            """
            This case checks, that user after clicking on 'Cart' button
            redirects to the Cart page
            """
            link = TestData.MAIN_PAGE_URL
            page = MainPage(browser, link)
            page.open_page(TestData.MAIN_PAGE_URL)
            page.redirection_to_the_cart_page()
            cart_page = page.getting_current_url()
            assert cart_page == TestData.CART_PAGE_URL, 'User not on the cart page'

        def test_checking_empty_cart(self, browser):
            """
            This case checks, that cart is empty, if user redirects to the cart page
            from main without any orders
            """
            link = TestData.MAIN_PAGE_URL
            page = MainPage(browser, link)
            page.open_page(TestData.MAIN_PAGE_URL)
            page.redirection_to_the_cart_page()
            checking_cart = page.checking_cart()
            assert checking_cart == TestData.EMPTY_CART, "The cart isn't empty..."

        def test_redirection_from_main_to_login_page(self, browser):
            """
            This case checks, that user after clicking on 'Sign in'
            button redirects to the login page
            """
            link = TestData.MAIN_PAGE_URL
            page = MainPage(browser, link)
            page.open_page(TestData.MAIN_PAGE_URL)
            page.redirection_to_the_login_page()
            login_page = page.getting_current_url()
            assert login_page == TestData.LOGIN_URL, "User isn't on the login page"

