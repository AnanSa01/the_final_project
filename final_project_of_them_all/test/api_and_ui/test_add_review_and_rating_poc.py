import unittest

from final_project_of_them_all.infra.api.api_wrapper import APIWrapper
from final_project_of_them_all.infra.config_provider import ConfigProvider
from final_project_of_them_all.infra.ui.browser_wrapper import BrowserWrapper
from final_project_of_them_all.logic.api.add_rating import AddRating
from final_project_of_them_all.logic.ui.home_page import HomePage
from final_project_of_them_all.logic.ui.login_page import LoginPage
from final_project_of_them_all.logic.ui.product_page import ProductPage
from final_project_of_them_all.logic.ui.search_page import SearchPage
from final_project_of_them_all.logic.utilities import LoadCon


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment for API and UI testing.

        Initializes APIWrapper for API requests and loads configuration data from a JSON file.
        """
        self._api_request = APIWrapper()
        self.config = LoadCon.return_config()

    def tearDown(self):
        """
        Clean up after each test.

        Closes the browser and performs any necessary cleanup tasks.
        """
        self.driver.quit()

    def test_add_review_api_and_ui_poc(self):
        """
        Proof-of-Concept (POC) Test Case for Adding and Verifying Reviews

        This POC test case demonstrates adding a review through the API and then verifying
        that the review appears correctly on the UI. It helps ensure that the end-to-end
        functionality of adding a review and its visibility on the product page is working.
        -----
        test case   #: 018
        requirement #: 005
        """
        api_add_rating = AddRating(self._api_request)
        item_id = self.config["add_rating_item_param"]
        payload_for_poc = self.config["payload_for_poc"]
        result_of_add_rating_api = api_add_rating.add_rating_api(item_id, payload_for_poc)
        print(result_of_add_rating_api.body)

        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.browser.config["base_url_login"])
        self.login_page = LoginPage(self.driver)
        self.login_page.write_in_email_input_field(self.config["email_input"])
        self.login_page.write_in_password_input_field(self.config["password_input"])
        self.login_page.click_on_sign_in_button()
        self.home_page = HomePage(self.driver)
        self.home_page.search_flow(self.config["poc_product_search"])
        self.search_page = SearchPage(self.driver)
        self.search_page.click_on_first_result()
        self.product_page = ProductPage(self.driver)
        payload_for_poc = self.config["payload_for_poc"]
        self.assertEqual(self.product_page.return_review_text(), payload_for_poc["comment"])


if __name__ == '__main__':
    unittest.main()
