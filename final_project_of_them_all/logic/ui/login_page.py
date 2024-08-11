import logging

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By

from final_project_of_them_all.logic.ui.base_page_app import BasePageApp


class LoginPage(BasePageApp):

    EMAIL_INPUT = '//input[@placeholder="Enter Email"]'
    PASSWORD_INPUT = '//input[@placeholder="Enter Password"]'
    SIGN_IN_BUTTON = '//form//button[@class="mt-3 btn btn-primary"]'
    LOGIN_ALERT_MESSAGE = '//div[@role="alert"]'
    GO_TO_SIGN_UP_BUTTON = '//a[@href="#/register?redirect=/"]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._email_input = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)
            self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
            self._sign_in_button = self._driver.find_element(By.XPATH, self.SIGN_IN_BUTTON)
            self._go_to_sign_up_button = self._driver.find_element(By.XPATH, self.GO_TO_SIGN_UP_BUTTON)

        except NoSuchElementException:
            logging.info("Error in initializing HomePage")

    def write_in_email_input_field(self, email):
        self._email_input.send_keys(email)

    def write_in_password_input_field(self, password):
        self._password_input.send_keys(password)

    def click_on_sign_in_button(self):
        self._sign_in_button.click()

    def check_if_login_alert_message_is_displayed(self):
        self._alert_message = self._driver.find_element(By.XPATH, self.LOGIN_ALERT_MESSAGE)
        return self._alert_message.is_displayed()

    def click_to_go_to_sign_up_button(self):
        self._go_to_sign_up_button.click()

    def login_flow(self, email, password):
        self.write_in_email_input_field(email)
        self.write_in_password_input_field(password)
        self.click_on_sign_in_button()

