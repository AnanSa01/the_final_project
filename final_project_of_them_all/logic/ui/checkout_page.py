import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from final_project_of_them_all.logic.ui.base_page_app import BasePageApp


class CheckoutPage(BasePageApp):
    ADDRESS_INPUT = '//input[@placeholder="Enter Address"]'
    CITY_INPUT = '//input[@placeholder="Enter City"]'
    POSTAL_CODE_INPUT = '//input[@placeholder="Enter Postal Code"]'
    COUNTRY_INPUT = '//input[@placeholder="Enter Country"]'
    CONTINUE_BUTTON = '//button[@class="my-3 btn btn-primary"]'
    METHOD_CONTINUE_BUTTON = '//button[@class="my-3 btn btn-primary"]'
    PLACE_ORDER_BUTTON = '//button[@class="w-100 btn btn-primary"]'
    CHOOSE_CREDIT_CARD_BUTTON = '//div[@data-funding-source="card"]//div'

    def __init__(self, driver):
        super().__init__(driver)
        self._address_input = self._driver.find_element(By.XPATH, self.ADDRESS_INPUT)
        self._city_input = self._driver.find_element(By.XPATH, self.CITY_INPUT)
        self._postal_code_input = self._driver.find_element(By.XPATH, self.POSTAL_CODE_INPUT)
        self._country_input = self._driver.find_element(By.XPATH, self.COUNTRY_INPUT)
        self._continue_button = self._driver.find_element(By.XPATH, self.CONTINUE_BUTTON)

    def write_in_address_input(self, address):
        self._address_input.send_keys(address)

    def write_in_city_input(self, city):
        self._city_input.send_keys(city)

    def write_in_postal_code_input(self, postal_code):
        self._postal_code_input.send_keys(postal_code)

    def write_in_country_input(self, country):
        self._country_input.send_keys(country)

    def click_on_continue_button(self):
        self._continue_button.click()

    def shipping_information_flow(self, address, city, postal_code, country):
        self.write_in_address_input(address)
        self.write_in_city_input(city)
        self.write_in_postal_code_input(postal_code)
        self.write_in_country_input(country)
        self.click_on_continue_button()

    def click_on_method_continue(self):
        self._method_continue_button = self._driver.find_element(By.XPATH, self.METHOD_CONTINUE_BUTTON)
        self._method_continue_button.click()

    def click_on_place_order_button(self):
        self._place_order_button = self._driver.find_element(By.XPATH, self.PLACE_ORDER_BUTTON)
        self._place_order_button.click()

    def click_on_credit_card_button(self):
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.CHOOSE_CREDIT_CARD_BUTTON)))
        self._credit_card_button = self._driver.find_element(By.XPATH, self.CHOOSE_CREDIT_CARD_BUTTON)
        self._credit_card_button.click()


