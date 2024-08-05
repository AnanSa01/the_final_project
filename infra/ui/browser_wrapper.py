import logging

from infra.logging_basicConfig import LoggingSetup
from selenium import webdriver
from infra.config_provider import ConfigProvider
from selenium.common.exceptions import *
from logic import utilities as UT


class BrowserWrapper:
    """
    this function takes instructions from the config file about the browser driver and the url site.
    """

    def __init__(self):
        self._driver = None
        try:

            self.config = UT.LoadCon.return_config()
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
