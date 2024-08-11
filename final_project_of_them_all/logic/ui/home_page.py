import logging
import time
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from final_project_of_them_all.logic.ui.base_page_app import BasePageApp


class HomePage(BasePageApp):
    SUCCESSFUL_LOGIN_MESSAGE = '//h1[contains(text(), "Latest Products")]'
    CHOOSE_ITEM = '//img[@class="card-img"]'
    NEXT_PAGE = '//a[@class="page-link"]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self.successful_login_message_function()

        except NoSuchElementException:
            logging.info("Error in initializing HomePage")

    def successful_login_message_function(self):
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.SUCCESSFUL_LOGIN_MESSAGE)))
        self._successful_login_message = self._driver.find_element(By.XPATH, self.SUCCESSFUL_LOGIN_MESSAGE)

    def return_displayed_successful_login_message(self):
        return self._successful_login_message.is_displayed()

    def click_on_first_item(self):
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.CHOOSE_ITEM)))
        self._choose_item = self._driver.find_element(By.XPATH, self.CHOOSE_ITEM)
        self._choose_item.click()

    def click_on_next_page(self):
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.NEXT_PAGE)))
        self._next_page_button = self._driver.find_element(By.XPATH, self.NEXT_PAGE)
        self._next_page_button.click()

