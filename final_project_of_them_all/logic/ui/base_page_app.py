import logging

from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait

from final_project_of_them_all.infra.ui.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class BasePageApp(BasePage):
    LOGIN_BUTTON = '//a[@href="#/login"]'
    USERNAME_BUTTON = '//a[@id="username"]'
    PROFILE_BUTTON = '//div[@class="dropdown-menu show"]//a[@href="#/profile"]'
    LOGOUT_BUTTON = '//div[@class="dropdown-menu show"]//a[@href="#"]'
    SEARCH_BAR = '//input[@class="mr-sm-2 ml-sm-5 form-control"]'
    SEARCH_SUBMIT_BUTTON = '//button[@class="p-2 mx-sm-2 btn btn-outline-success"]'
    CART_BUTTON = '//a[@href="#/cart"]'
    LOGO_BUTTON = '//img[@alt="Otaku Shop"]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._login_button = self._driver.find_element(By.XPATH, self.LOGIN_BUTTON)
            self._logo_button = self._driver.find_element(By.XPATH, self.LOGO_BUTTON)

        except NoSuchElementException:
            logging.info("Error in initializing BasePageApp")

    def click_on_login_button_in_header(self):
        self._login_button.click()

    def click_on_settings_button_in_header(self):
        self._settings_button = self._driver.find_element(By.XPATH, self.USERNAME_BUTTON)
        self._settings_button.click()

    def click_on_profile_button_flow_in_header(self):
        self.click_on_settings_button_in_header()
        self._profile_button = self._driver.find_element(By.XPATH, self.PROFILE_BUTTON)
        self._profile_button.click()

    def click_on_logout_button_flow_in_header(self):
        self.click_on_settings_button_in_header()
        self._logout_button = self._driver.find_element(By.XPATH, self.LOGOUT_BUTTON)
        self._logout_button.click()

    def click_on_cart_button_in_header(self):
        self._cart_button = self._driver.find_element(By.XPATH, self.CART_BUTTON)
        self._cart_button.click()

    def search_flow(self, search_input):
        self.search_bar_function()
        self._search_bar.send_keys(search_input)
        self.search_submit_button_function()
        self._search_submit_button.click()

    def search_bar_function(self):
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.SEARCH_BAR)))
        self._search_bar = self._driver.find_element(By.XPATH, self.SEARCH_BAR)

    def search_submit_button_function(self):
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.SEARCH_SUBMIT_BUTTON)))
        self._search_submit_button = self._driver.find_element(By.XPATH, self.SEARCH_SUBMIT_BUTTON)
