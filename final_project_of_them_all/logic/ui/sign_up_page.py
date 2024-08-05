from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from final_project_of_them_all.logic.ui.base_page_app import BasePageApp


class SignUpPage(BasePageApp):
    ENTER_NAME_INPUT = '//input[@placeholder="Enter Name"]'
    ENTER_EMAIL_INPUT = '//input[@placeholder="Enter Email"]'
    ENTER_PASSWORD_INPUT = '//input[@placeholder="Enter Password"]'
    RE_ENTER_PASSWORD_INPUT = '//input[@placeholder="Confirm Password"]'
    REGISTER_BUTTON = '//main//button[@type="submit"]'
    SIGN_UP_ALERT_MESSAGE = '//div[@role="alert"]'
    REGISTER_TITLE = '//h1[contains(text(), "Register")]'

    def __init__(self, driver):
        super().__init__(driver)
        self._name_input = self._driver.find_element(By.XPATH, self.ENTER_NAME_INPUT)
        self._email_input = self._driver.find_element(By.XPATH, self.ENTER_EMAIL_INPUT)
        self._password_input = self._driver.find_element(By.XPATH, self.ENTER_PASSWORD_INPUT)
        self._re_password_input = self._driver.find_element(By.XPATH, self.RE_ENTER_PASSWORD_INPUT)


    def enter_name_function(self, name_input):
        self._name_input.send_keys(name_input)

    def enter_email_function(self, email_input):
        self._email_input.send_keys(email_input)

    def enter_password_function(self, password_input):
        self._password_input.send_keys(password_input)

    def re_enter_password_function(self, re_password_input):
        self._re_password_input.send_keys(re_password_input)

    def enter_and_re_enter_password_flow(self, password_input):
        self.enter_password_function(password_input)
        self.re_enter_password_function(password_input)

    def click_on_register_button(self):
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.REGISTER_BUTTON)))
        self._register_button = self._driver.find_element(By.XPATH, self.REGISTER_BUTTON)
        self._register_button.click()

    def check_if_sign_up_alert_message_is_displayed(self):
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.SIGN_UP_ALERT_MESSAGE)))
        self._alert_message = self._driver.find_element(By.XPATH, self.SIGN_UP_ALERT_MESSAGE)
        return self._alert_message.is_displayed()

    def check_if_still_on_register_page(self):
        self._register_title = self._driver.find_element(By.XPATH, self.REGISTER_TITLE)
        return self._register_title.is_displayed()


