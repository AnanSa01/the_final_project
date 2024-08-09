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

    def test_add_item_in_quantity_to_cart(self):
        self.home_page.click_on_first_item()
        self.product_page = ProductPage(self.driver)
        quantity_input = random.randint(1, 10)
        self.product_page.click_add_to_cart_in_quantity_flow(quantity_input)
        self.product_page.click_on_add_to_cart_button()
        self.product_page.click_on_cart_button_in_header()
        self.cart_page = CartPage(self.driver)
        self.cart_page.click_on_proceed_to_checkout_button()
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.shipping_information_flow(self.config["shipping_address_input"],
                                                     self.config["shipping_city_input"],
                                                     self.config["shipping_postal_code_input"],
                                                     self.config["shipping_country_input"])
        self.checkout_page.click_on_method_continue()
        self.assertEqual(quantity_input, self.checkout_page.return_quantity_of_order_details())


if __name__ == '__main__':
    unittest.main()
