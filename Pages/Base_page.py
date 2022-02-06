from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.Main_page_locators import MainPageLocators as main_page_locators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_page(self, url):
        self.browser.get(url)

    def search_element(self, locator, time=5):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")
