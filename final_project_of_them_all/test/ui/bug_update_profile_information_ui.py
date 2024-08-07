import time
import unittest

from final_project_of_them_all.infra.ui.browser_wrapper import BrowserWrapper
from final_project_of_them_all.logic import utilities as LUT
from final_project_of_them_all.infra.utilities import Utilities as IUT
from final_project_of_them_all.logic.ui.home_page import HomePage
from final_project_of_them_all.logic.ui.login_page import LoginPage
from final_project_of_them_all.logic.ui.profile_page import ProfilePage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = LUT.LoadCon.return_config()
        self.driver = self.browser.get_driver(self.config["base_url_login"])
        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config["email_input"], self.config["password_input"])
        self.home_page = HomePage(self.driver)

    def test_update_profile_information_function(self):
        self.home_page.click_on_profile_button_flow_in_header()
        self.profile_page = ProfilePage(self.driver)
        self.profile_page.update_profile_information_flow(self.config["update_name_input"], self.config["email_input"],
                                                          IUT.generate_random_string_just_numbers(
                                                              self.config["update_password_length"]))
        self.assertEqual(self.profile_page.return_updated_information_success_text(),
                         self.config["update_profile_information_success_message"])


if __name__ == '__main__':
    unittest.main()
