import logging

from selenium import webdriver
from selenium.common.exceptions import *
from final_project_of_them_all.logic.utilities import LoadJSON


class BrowserWrapper:
    """
    this function takes instructions from the config file about the browser driver and the url site.
    """

    def __init__(self):
        self._driver = None
        try:

            self.config = LoadJSON.return_config()
        except NoSuchElementException:
            logging.error("Error in finding element in BrowserWrapper")
        print("\nTest Start")

    def get_driver(self, url):
        try:
            if self.config["browser"] == "Chrome":
                self._driver = webdriver.Chrome()
            elif self.config["browser"] == "FireFox":
                self._driver = webdriver.Firefox()
            elif self.config["browser"] == "Edge":
                self._driver = webdriver.Edge()

            self._driver.get(url)
            self._driver.maximize_window()
            return self._driver
        except WebDriverException:
            logging.error("There is an error while opening the browser")
