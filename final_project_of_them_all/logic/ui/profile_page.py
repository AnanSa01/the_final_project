import logging

from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from final_project_of_them_all.logic.ui.base_page_app import BasePageApp


class ProfilePage(BasePageApp):

    NAME_INPUT = '//input[@placeholder="Enter Name"]'
    EMAIL_INPUT = '//input[@placeholder="Enter Email"]'
    PASSWORD_INPUT = '//input[@placeholder="Enter Password"]'
    RE_PASSWORD_INPUT = '//input[@placeholder="Confirm Password"]'
    UPDATE_BUTTON = '//button[@class="mt-3 btn btn-primary"]'
    TITLE_TEXT = '//div[contains(text(), "Successfully Updated")]'

    def __init__(self, driver):
        try:
            super().__init__(driver)
            self._name_input = self._driver.find_element(By.XPATH, self.NAME_INPUT)
            self._email_input = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)
            self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
            self._re_password_input = self._driver.find_element(By.XPATH, self.RE_PASSWORD_INPUT)
            self._update_button = self._driver.find_element(By.XPATH, self.UPDATE_BUTTON)

        except NoSuchElementException:
            logging.info("Error in initializing ProfilePage")

    def write_in_name_input(self, name):
        self._name_input.send_keys(name)

    def write_in_email_input(self, email):
        self._email_input.send_keys(email)

    def write_in_password_input(self, password):
        self._password_input.send_keys(password)

    def write_in_re_password_input(self, re_password):
        self._re_password_input.send_keys(re_password)

    def click_on_update_button(self):
        self._update_button.click()

    def update_profile_information_flow(self, name, email, password):
        self.write_in_name_input(name)
        self.write_in_email_input(email)
        self.write_in_password_input(password)
        self.write_in_re_password_input(password)
        self.click_on_update_button()

    def return_updated_information_success_text(self):
        self._title_text = self._driver.find_element(By.XPATH, self.TITLE_TEXT)
        return self._title_text.text

    