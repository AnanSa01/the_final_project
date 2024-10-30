import logging
import unittest
from final_project_of_them_all.infra.ui.browser_wrapper import BrowserWrapper
from final_project_of_them_all.logic.ui.cart_page import CartPage
from final_project_of_them_all.logic.ui.home_page import HomePage
from final_project_of_them_all.logic.ui.login_page import LoginPage
from final_project_of_them_all.logic.ui.product_page import ProductPage
from final_project_of_them_all.logic.utilities import LoadJSON


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

        Closes the browser.
        """
        self.driver.close()
        logging.info(f'End of test. {self.config["browser"]} web driver is closed.\n')

    def test_remove_from_cart(self):
        """
        Test case for adding an item to the cart and then removing it.

        This test verifies that an item can be added to the cart and subsequently removed,
        and checks that the cart is empty after removal.
        -----
        test case   #: 019
        requirement #: 007
        """
        logging.info("Initialize Test: remove item from cart with UI")

        # Select an item and add it to the cart
        self.home_page.click_on_first_item()
        self.product_page = ProductPage(self.driver)
        self.product_page.click_on_add_to_cart_button()

        # Navigate to cart, remove the item
        self.product_page.click_on_cart_button_in_header()
        self.cart_page = CartPage(self.driver)
        self.cart_page.remove_item_from_cart()

        # Verify cart is empty
        self.assertTrue(self.cart_page.return_true_if_cart_is_empty())


if __name__ == '__main__':
    unittest.main()
