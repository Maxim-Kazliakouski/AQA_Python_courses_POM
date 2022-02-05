from selenium.webdriver.common.by import By


class CartPageLocators:

    CART_BUTTON = By.XPATH, '//*[@id="header"]/div[3]/div/div/div[3]/div/a'
    EMPTY_CART = By.CLASS_NAME, 'ajax_cart_no_product'
    LOGIN_BUTTON = By.CLASS_NAME, 'login'
    MAIN_LOGO_BUTTON = By.XPATH, '//*[@id="header_logo"]/a'




