from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from final_project_of_them_all.logic.ui.base_page_app import BasePageApp


class ProductPage(BasePageApp):
    ADD_TO_CART_BUTTON = '//button[@class="w-100 btn btn-primary"]'
    RATING_INPUT = '//select[@id="rating"]'
    REVIEW_TEXT = '//div[@class="col-md-6"]//p[2]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            ...
        except NoSuchElementException:
            print("error")

    def click_on_add_to_cart_button(self):
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ADD_TO_CART_BUTTON)))
        self._add_to_cart_button = self._driver.find_element(By.XPATH, self.ADD_TO_CART_BUTTON)
        self._add_to_cart_button.click()

    def click_on_rating_input(self):
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.RATING_INPUT)))
        self._rating_input = self._driver.find_element(By.XPATH, self.RATING_INPUT)
        self._rating_input.click()

    def return_review_text(self):
        WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.REVIEW_TEXT)))
        self._review_text = self._driver.find_element(By.XPATH, self.REVIEW_TEXT)
        print(self._review_text.text)
        return self._review_text.text







