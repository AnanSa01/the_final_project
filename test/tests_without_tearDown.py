import unittest

from infra.ui.browser_wrapper import BrowserWrapper
from logic.ui.home_page import HomePage
from logic.ui.login_page import LoginPage
from logic import utilities as UT
from logic.ui.search_page import SearchPage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = UT.LoadCon.return_config()
        self.driver = self.browser.get_driver(self.config["base_url_login"])
        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config["email_input"], self.config["password_input"])
        self.home_page = HomePage(self.driver)

    def test_search_function(self):
        self.home_page.search_flow(self.config["search_for_item"])
        self.search_page = SearchPage(self.driver)
        self.assertEqual(self.search_page.return_result_titles(), self.config["search_for_item"])



if __name__ == '__main__':
    unittest.main()
