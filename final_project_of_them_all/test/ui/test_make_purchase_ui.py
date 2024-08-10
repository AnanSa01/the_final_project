import time
import unittest
from final_project_of_them_all.logic.utilities import LoadCon
from final_project_of_them_all.infra.utilities import Utilities as IUT
from final_project_of_them_all.infra.ui.browser_wrapper import BrowserWrapper
from final_project_of_them_all.logic.ui.cart_page import CartPage
from final_project_of_them_all.logic.ui.checkout_page import CheckoutPage
from final_project_of_them_all.logic.ui.home_page import HomePage
from final_project_of_them_all.logic.ui.login_page import LoginPage
from final_project_of_them_all.logic.ui.product_page import ProductPage
from final_project_of_them_all.logic.ui.search_page import SearchPage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment for UI testing.

        Initializes the browser, loads configuration data, and performs login.
        """
        self.browser = BrowserWrapper()
        self.config = LoadCon.return_config()
        self.driver = self.browser.get_driver(self.config["base_url_login"])
        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config["email_input"], self.config["password_input"])
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        """
        Clean up after each test by closing the browser.
        """
        self.driver.close()

    def test_make_purchase(self):
        """
        Test case for making a purchase on the website.

        This test verifies that a user can:
        - Search for an item
        - Add it to the cart
        - Proceed through checkout
        - Enter shipping and billing information
        - Complete the purchase and receive a confirmation message.
        -----
        test case   #: 020
        requirement #: 007
        """
        # Search for the item and add it to the cart
        self.home_page.search_flow(self.config["make_purchase_item"])
        self.search_page = SearchPage(self.driver)
        self.search_page.click_on_first_result()
        self.product_page = ProductPage(self.driver)
        self.product_page.click_on_add_to_cart_button()

        # Proceed to checkout and enter information
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
        self.checkout_page.billing_flow(self.config["billing_country"], self.config["billing_fake_credit_card_number"],
                                        self.config["billing_fake_credit_card_expire_date"],
                                        IUT.generate_random_string_just_numbers(3),
                                        self.config["name_input"].title(), self.config["last_name_input"].title(),
                                        self.config["billing_street"],
                                        self.config["billing_more_details"], self.config["billing_city"],
                                        self.config["billing_zip_code"], self.config["billing_phone_number"],
                                        self.config["email_input"])

        # Verify the purchase confirmation
        self.assertIn(self.config["purchase_confirmation"], self.checkout_page.return_alert_message_in_purchase())


if __name__ == '__main__':
    unittest.main()
