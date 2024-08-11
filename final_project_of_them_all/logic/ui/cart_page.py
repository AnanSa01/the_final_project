import logging

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from final_project_of_them_all.logic.ui.base_page_app import BasePageApp


class CartPage(BasePageApp):
    ITEMS_IN_CART = '//div[@class="list-group-item"]//img'
    REMOVE_FROM_CART_BUTTON = '//div[@class="list-group-item"]//button[@class="btn btn-light"]'
    CHECKOUT_BUTTON = '//button[@class="w-100 btn btn-primary"]'
    QUANTITY_BUTTON = '//div[@class="col-md-3"]'
    EMPTY_CART_ALERT = '//div[contains(text(), "Your cart is empty.")]'

    def __init__(self, driver):
        try:
            super().__init__(driver)
            self._item_in_cart = self._driver.find_element(By.XPATH, self.ITEMS_IN_CART)
            self._remove_from_cart_button = self._driver.find_element(By.XPATH, self.REMOVE_FROM_CART_BUTTON)
            

        except NoSuchElementException:
            logging.info("Error in initializing CartPage")


    def return_true_if_cart_not_empty(self):
        return self._item_in_cart.is_displayed()

    def return_true_if_cart_is_empty(self):
        WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.EMPTY_CART_ALERT)))
        self._empty_cart_alert = self._driver.find_element(By.XPATH, self.EMPTY_CART_ALERT)
        return self._empty_cart_alert.is_displayed()

    def remove_item_from_cart(self):
        self._remove_from_cart_button.click()

    def click_on_proceed_to_checkout_button(self):
        WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located((By.XPATH, self.CHECKOUT_BUTTON)))
        self._proceed_to_checkout_button = self._driver.find_element(By.XPATH, self.CHECKOUT_BUTTON)
        self._proceed_to_checkout_button.click()


