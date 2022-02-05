from Locators.Main_page_locators import MainPageLocators as main_page_locators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open_page(self, url):
        self.browser.get(url)


    # def search_element_by(self, locator):
    #     self.browser.find_element(locator)
