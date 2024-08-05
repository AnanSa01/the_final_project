import time
import unittest

from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider
from infra.ui.browser_wrapper import BrowserWrapper
from logic.api.add_rating import AddRating
from logic.ui.home_page import HomePage
from logic.ui.login_page import LoginPage
from logic.ui.product_page import ProductPage
from logic.ui.search_page import SearchPage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        ...

    def test_add_review_both(self):
        self._api_request = APIWrapper()
        api_add_rating = AddRating(self._api_request)
        result = api_add_rating.add_rating_api()
        print(result.body)

        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.browser.config["base_url_login"])
        self.login_page = LoginPage(self.driver)
        self.config = ConfigProvider.load_from_file('../config.json')
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
