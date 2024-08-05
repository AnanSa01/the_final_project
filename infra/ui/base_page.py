from selenium import webdriver


class BasePage:

    def __init__(self, driver):
        self._driver = driver

    def refresh_page(self):
        """
        this function to refresh page from everywhere in the website.
        """
        self._driver.refresh()

    def back_func(self):
        """
        this function to turn back page from everywhere in the website.
        """
        self._driver.back()
