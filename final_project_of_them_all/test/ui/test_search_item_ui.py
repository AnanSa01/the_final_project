import unittest

from final_project_of_them_all.infra.ui.browser_wrapper import BrowserWrapper
from final_project_of_them_all.logic.ui.home_page import HomePage
from final_project_of_them_all.logic.ui.login_page import LoginPage
from final_project_of_them_all.logic import utilities as UT
from final_project_of_them_all.logic.ui.search_page import SearchPage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment for UI testing.

        Initializes the browser, loads configuration data, and performs login.
        """
        self.browser = BrowserWrapper()
        self.config = UT.LoadCon.return_config()
        self.driver = self.browser.get_driver(self.config["base_url_login"])
        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config["email_input"], self.config["password_input"])
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        """
        Clean up after each test by closing the browser.
        """
        self.driver.close()

    def test_search_function(self):
        """
        Test case for searching items on the website.

        This test verifies that the search function returns results matching the search query.
        -----
        test case   #: 015
        requirement #: 005
        """
        self.home_page.search_flow(self.config["search_for_item"])
        self.search_page = SearchPage(self.driver)
        self.assertEqual(self.search_page.return_result_titles(), self.config["search_for_item"])



if __name__ == '__main__':
    unittest.main()
