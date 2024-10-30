import logging
import random
import unittest

from final_project_of_them_all.logic.utilities import LoadJSON
from final_project_of_them_all.infra.ui.browser_wrapper import BrowserWrapper
from final_project_of_them_all.logic.ui.cart_page import CartPage
from final_project_of_them_all.logic.ui.checkout_page import CheckoutPage
from final_project_of_them_all.logic.ui.home_page import HomePage
from final_project_of_them_all.logic.ui.login_page import LoginPage
from final_project_of_them_all.logic.ui.product_page import ProductPage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment for UI testing.

        Initializes the browser, loads configuration data, and performs login.
        """
        self.browser = BrowserWrapper()
        self.config = LoadJSON.return_config()
        self.driver = self.browser.get_driver(self.config["base_url_login"])
        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config["email_input"], self.config["password_input"])
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        """
        Clean up after each test.

        Closes the browser and performs any necessary cleanup tasks.
        """
        self.driver.close()
        logging.info(f'End of test. {self.config["browser"]} web driver is closed.\n')

    def test_add_item_in_quantity_to_cart(self):
        """
        Test case for adding an item with a specified quantity to the cart and verifying it during checkout.

        This test verifies that an item can be added to the cart with a specific quantity and that the
        quantity is correctly reflected during the checkout process.
        -----
        test case   #: 018
        requirement #: 007
        """
        logging.info("Initialize Test: add item to cart in quantity with UI")

        # Select and add item to the cart
        self.home_page.click_on_first_item()
        self.product_page = ProductPage(self.driver)
        quantity_input = random.randint(self.config["random_from"], self.config["random_to"])  # Random quantity number
        self.product_page.click_add_to_cart_in_quantity_flow(quantity_input)
        self.product_page.click_on_add_to_cart_button()

        # Navigate to cart and proceed to checkout
        self.product_page.click_on_cart_button_in_header()
        self.cart_page = CartPage(self.driver)
        self.cart_page.click_on_proceed_to_checkout_button()

        # Complete checkout process
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.shipping_information_flow(self.config["shipping_address_input"],
                                                     self.config["shipping_city_input"],
                                                     self.config["shipping_postal_code_input"],
                                                     self.config["shipping_country_input"])
        self.checkout_page.click_on_method_continue()

        # Verify that the quantity in the checkout details matches the quantity added
        self.assertEqual(quantity_input, self.checkout_page.return_quantity_of_order_details())


if __name__ == '__main__':
    unittest.main()
