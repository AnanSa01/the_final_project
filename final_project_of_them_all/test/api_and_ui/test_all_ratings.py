import logging
import unittest
from final_project_of_them_all.infra.api.api_wrapper import APIWrapper
from final_project_of_them_all.infra.ui.browser_wrapper import BrowserWrapper
from final_project_of_them_all.logic.api.get_all_products import Products
from final_project_of_them_all.logic.api_and_ui.test_all_ratings_api_and_ui import AllRatings
from final_project_of_them_all.logic.ui.home_page import HomePage
from final_project_of_them_all.logic.ui.login_page import LoginPage
from final_project_of_them_all.logic.utilities import LoadCon


class MyTestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment for API and UI testing.

        Initializes the API wrapper, browser, configuration data, and performs login.
        """
        self._api_request = APIWrapper()
        self.config = LoadCon.return_config()
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.config["base_url_login"])
        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config["email_input"], self.config["password_input"])
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        """
        Clean up after tests.

        Closes the browser after test execution.
        """
        self.driver.close()

    def test_all_ratings(self):
        """
        Test case for verifying ratings for multiple items.

        This test performs the following steps:
        1. Retrieves the IDs of all items from the UI.
        2. Sends API requests to rate five random items with ratings from 1 to 5.
        3. Sends another API requests for products to retrieve a list of all products' information.
        4. Gathers all updated review information into a list, to include it with the product ID and name for each item.
        5. Checks if the ratings for each item match the expected results in the UI.

        The test ensures that all items have correct ratings by validating the list of results contains all True values.
        -----
        test case   #: 013
        requirement #: 004
        """
        logging.info("Initialize Test: verify different ratings for multiple items. with API & UI - POC")

        # Get IDs of all items through UI, and rate five random items with ratings from 1 to 5 with API.
        self.all_ratings = AllRatings(self.driver)
        all_details = self.all_ratings.give_to_five_items_rating(self._api_request)

        # Retrieve updated product data from another API request with reviews details.
        api_get_products = Products(self._api_request)
        result_of_products = api_get_products.get_products_api()
        products = result_of_products.body["products"]

        # Gather updated rating details including new ratings and reviews for the items
        all_details_updated = self.all_ratings.gather_all_details_for_items(all_details, products)

        # Check if all ratings are correctly reflected in the UI
        list_with_result_of_five_tests = self.all_ratings.check_all_ratings_for_item(self.driver, all_details_updated)
        details_with_result = list_with_result_of_five_tests + all_details_updated
        self.assertTrue(all(list_with_result_of_five_tests), details_with_result)


if __name__ == '__main__':
    unittest.main()
