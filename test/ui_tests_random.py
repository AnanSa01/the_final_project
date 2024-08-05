import time
import unittest
from logic import utilities as UT
from infra.ui.browser_wrapper import BrowserWrapper
from logic.ui.cart_page import CartPage
from logic.ui.home_page import HomePage
from logic.ui.login_page import LoginPage
from logic.ui.product_page import ProductPage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = UT.LoadCon.return_config()
        self.driver = self.browser.get_driver(self.config["base_url_login"])
        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config["email_input"], self.config["password_input"])
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.cart_page.remove_item_from_cart()
        self.driver.close()

    def test_add_to_cart(self):
        self.home_page.click_on_first_item()
        self.product_page = ProductPage(self.driver)
        self.product_page.click_on_add_to_cart_button()
        self.product_page.click_on_cart_button_in_header()
        self.cart_page = CartPage(self.driver)
        self.assertTrue(self.cart_page.return_true_if_cart_not_empty())



if __name__ == '__main__':
    unittest.main()
