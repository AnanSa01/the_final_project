import unittest
from final_project_of_them_all.infra.api.api_wrapper import APIWrapper
from final_project_of_them_all.infra.ui.browser_wrapper import BrowserWrapper
from final_project_of_them_all.logic.ui.home_page import HomePage
from final_project_of_them_all.logic.ui.login_page import LoginPage
from final_project_of_them_all.logic.utilities import LoadCon


class MyTestCase(unittest.TestCase):

    def test_all_ratings(self):
        self.config = LoadCon.return_config()
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.browser.config["base_url_login"])
        self.login_page = LoginPage(self.driver)
        self.login_page.write_in_email_input_field(self.config["email_input"])
        self.login_page.write_in_password_input_field(self.config["password_input"])
        self.login_page.click_on_sign_in_button()
        self.home_page = HomePage(self.driver)


if __name__ == '__main__':
    unittest.main()
