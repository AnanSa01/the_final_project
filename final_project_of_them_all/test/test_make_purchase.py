import time
import unittest
from final_project_of_them_all.logic import utilities as UT
from final_project_of_them_all.infra.ui.browser_wrapper import BrowserWrapper
from final_project_of_them_all.logic.ui.cart_page import CartPage
from final_project_of_them_all.logic.ui.checkout_page import CheckoutPage
from final_project_of_them_all.logic.ui.home_page import HomePage
from final_project_of_them_all.logic.ui.login_page import LoginPage
from final_project_of_them_all.logic.ui.product_page import ProductPage
from final_project_of_them_all.logic.ui.search_page import SearchPage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = UT.LoadCon.return_config()
        self.driver = self.browser.get_driver(self.config["base_url_login"])
        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config["email_input"], self.config["password_input"])
        self.home_page = HomePage(self.driver)

    def test_make_purchase(self):
        self.home_page.search_flow(self.config["make_purchase_item"])
        self.search_page = SearchPage(self.driver)
        self.search_page.click_on_first_result()
        self.product_page = ProductPage(self.driver)
        self.product_page.click_on_add_to_cart_button()
        self.cart_page = CartPage(self.driver)
        self.cart_page.click_on_proceed_to_checkout_button()
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.shipping_information_flow(self.config["shipping_address_input"],
                                                     self.config["shipping_city_input"],
                                                     self.config["shipping_postal_code_input"],
                                                     self.config["shipping_country_input"])
        self.checkout_page.click_on_method_continue()
        self.checkout_page.click_on_place_order_button()
        self.checkout_page.click_on_credit_card_button()


if __name__ == '__main__':
    unittest.main()
