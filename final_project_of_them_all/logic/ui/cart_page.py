from selenium.webdriver.common.by import By

from final_project_of_them_all.logic.ui.base_page_app import BasePageApp


class CartPage(BasePageApp):
    ITEMS_IN_CART = '//div[@class="list-group-item"]//img'
    REMOVE_FROM_CART_BUTTON = '//div[@class="list-group-item"]//button[@class="btn btn-light"]'
    CHECKOUT_BUTTON = '//button[@class="w-100 btn btn-primary"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._item_in_cart = self._driver.find_element(By.XPATH, self.ITEMS_IN_CART)
        self._remove_from_cart_button = self._driver.find_element(By.XPATH, self.REMOVE_FROM_CART_BUTTON)
        self._proceed_to_checkout_button = self._driver.find_element(By.XPATH, self.CHECKOUT_BUTTON)


    def return_true_if_cart_not_empty(self):
        return self._item_in_cart.is_displayed()

    def remove_item_from_cart(self):
        self._remove_from_cart_button.click()

    def click_on_proceed_to_checkout_button(self):
        self._proceed_to_checkout_button.click()
