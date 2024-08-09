import random
import unittest
from final_project_of_them_all.logic import utilities as UT
from final_project_of_them_all.infra.ui.browser_wrapper import BrowserWrapper
from final_project_of_them_all.logic.ui.cart_page import CartPage
from final_project_of_them_all.logic.ui.checkout_page import CheckoutPage
from final_project_of_them_all.logic.ui.home_page import HomePage
from final_project_of_them_all.logic.ui.login_page import LoginPage
from final_project_of_them_all.logic.ui.product_page import ProductPage
from selenium.webdriver.support.ui import Select



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = UT.LoadCon.return_config()
        self.driver = self.browser.get_driver(self.config["base_url_login"])
        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config["email_input"], self.config["password_input"])
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_add_to_cart(self):
        self.home_page.click_on_first_item()
        self.product_page = ProductPage(self.driver)
        self.product_page.click_on_add_to_cart_button()
        self.product_page.click_on_cart_button_in_header()
        self.cart_page = CartPage(self.driver)
        self.cart_page.remove_item_from_cart()
        self.assertTrue(self.cart_page.return_true_if_cart_is_empty())



if __name__ == '__main__':
    unittest.main()
