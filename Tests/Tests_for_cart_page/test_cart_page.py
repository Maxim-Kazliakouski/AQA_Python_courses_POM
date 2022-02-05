from Tests.Tests_for_cart_page.data_cart_page import TestData
from Pages.Cart_page import CartPage
import time


class Test_for_cart_page:
    class Test_positive:
        def test_user_on_cart_page(self, browser):
            """
            This case checks, that user gets to the cart page
            """
            link = TestData.CART_PAGE_URL
            page = CartPage(browser, link)
            page.open_page(TestData.CART_PAGE_URL)
            cart_page = page.getting_current_url()
            assert cart_page == TestData.CART_PAGE_URL, "User isn't on cart page"

        def test_redirection_from_cart_to_main_page(self, browser):
            """
            This case checks, that user after clicking on 'Main logo' button
            redirects to the Main page
            """
            link = TestData.CART_PAGE_URL
            page = CartPage(browser, link)
            page.open_page(TestData.CART_PAGE_URL)
            page.redirection_to_the_main_page()
            main_page = page.getting_current_url()
            assert main_page == TestData.MAIN_PAGE_URL, "User isn't on main page"

    def test_checking_empty_cart(self, browser):
        """
        This case checks, that cart is empty, if user on the cart page
        from main without any orders
        """
        link = TestData.CART_PAGE_URL
        page = CartPage(browser, link)
        page.open_page(TestData.CART_PAGE_URL)
        checking_cart = page.checking_cart()
        assert checking_cart == TestData.EMPTY_CART, "The cart isn't empty..."

    def test_redirection_from_cart_to_login_page(self, browser):
        """
        This case checks, that user after clicking on 'Sign in'
        button redirects to the login page
        """
        link = TestData.CART_PAGE_URL
        page = CartPage(browser, link)
        page.open_page(TestData.CART_PAGE_URL)
        page.redirection_to_the_login_page()
        login_page = page.getting_current_url()
        assert login_page == TestData.LOGIN_URL, "User isn't on the login page"

