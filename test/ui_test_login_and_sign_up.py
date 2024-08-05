import logging
import unittest

from infra.logging_basicConfig import LoggingSetup
from infra.ui.browser_wrapper import BrowserWrapper
from logic.ui.home_page import HomePage
from logic import utilities as UT
from infra.utilities import Utilities
from logic.ui.login_page import LoginPage
from logic.ui.sign_up_page import SignUpPage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        this setUp just for opening a browser with a selected driver
        """
        self.browser = BrowserWrapper()
        self.config = UT.LoadCon.return_config()
        self.driver = self.browser.get_driver(self.config["base_url_login"])
        logging.info(f'UI Test. Opening a {self.browser.config["browser"]} web driver.')
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        """
        this tearDown just for closing the browser after finishing testing.
        """
        self.driver.close()
        logging.info(f'---------- End of test. {self.browser.config["browser"]} web driver is closed. ----------\n')

    def test_valid_login(self):
        """
        this function tests valid login input for a user.
        -----
        test case   #: 001
        requirement #: 001
        """
        logging.info("---------- Initialize Test: valid login ----------")
        self.login_page.write_in_email_input_field(self.config["email_input"])
        self.login_page.write_in_password_input_field(self.config["password_input"])
        self.login_page.click_on_sign_in_button()
        self.home_page = HomePage(self.driver)
        self.home_page.return_displayed_successful_login_message()
        self.assertTrue(self.home_page.return_displayed_successful_login_message())

    def test_not_adding_password_in_login(self):
        """
        this function ensures the website does not connect when only entering user input without password.
        -----
        test case   #: 002
        requirement #: 002
        """
        logging.info("---------- Initialize Test: not adding password in login ----------")
        self.login_page.write_in_email_input_field(self.config["email_input"])
        self.login_page.click_on_sign_in_button()
        self.assertTrue(self.login_page.check_if_login_alert_message_is_displayed(), "Error! Should NOT connect")
        logging.info("assertTrue if alert message is displayed")

    def test_not_adding_password_nor_email_in_login(self):
        """
        this function ensures the website does not connect when NOT entering user input nor password.
        -----
        test case   #: 003
        requirement #: 002
        """
        logging.info("---------- Initialize Test: not adding password in login ----------")
        self.login_page.click_on_sign_in_button()
        self.assertTrue(self.login_page.check_if_login_alert_message_is_displayed(), "Error! Should NOT be able to connect")
        logging.info("assertTrue if alert message is displayed")

    def test_sign_up_with_already_connected_user(self):
        """
        this function tests trying to sign up with input of an already connected user.
        -----
        test case   #: 004
        requirement #: 003
        """
        logging.info("---------- Initialize Test: signing up with already connected user ----------")
        self.login_page.click_to_go_to_sign_up_button()
        self.sign_up_page = SignUpPage(self.driver)
        self.sign_up_page.enter_name_function(self.config["name_input"])
        self.sign_up_page.enter_email_function(self.config["email_input"])
        self.sign_up_page.enter_and_re_enter_password_flow(self.config["password_input"])
        self.sign_up_page.click_on_register_button()
        self.assertTrue(self.sign_up_page.check_if_sign_up_alert_message_is_displayed(),
                        "Error! Should NOT connect")
        logging.info("assertTrue if alert message is displayed")

    def test_invalid_email_sign_up(self):
        """
        this function tests signing up with invalid email input.
        -----
        test case   #: 005
        requirement #: 003
        """
        logging.info("---------- Initialize Test: invalid Email sign up ----------")
        self.login_page.click_to_go_to_sign_up_button()
        self.sign_up_page = SignUpPage(self.driver)
        self.sign_up_page.enter_name_function(Utilities.generate_random_string_just_text(5))
        self.sign_up_page.enter_email_function(Utilities.generate_random_string_just_punctuation(10))
        self.sign_up_page.enter_and_re_enter_password_flow(Utilities.generate_random_string_just_numbers(8))
        self.sign_up_page.click_on_register_button()
        self.assertTrue(self.sign_up_page.check_if_still_on_register_page(), "Error! Should NOT connect")
        logging.info("assertTrue if alert message is displayed")

    def test_password_not_match_re_enter_password(self):
        """
        this function tests input of password not matching input of re-enter password.
        -----
        test case   #: 006
        requirement #: 003
        """
        logging.info("---------- Initialize Test: password not matching re-entering password ----------")
        self.login_page.click_to_go_to_sign_up_button()
        self.sign_up_page = SignUpPage(self.driver)
        self.sign_up_page.enter_name_function(Utilities.generate_random_string_just_text(5))
        self.sign_up_page.enter_email_function(self.config["email_input"])
        self.sign_up_page.enter_password_function(Utilities.generate_random_string_just_numbers(8))
        self.sign_up_page.re_enter_password_function(Utilities.generate_random_string_just_numbers(9))
        self.sign_up_page.click_on_register_button()
        self.assertTrue(self.sign_up_page.check_if_sign_up_alert_message_is_displayed(),
                        "Error! Should NOT be able to connect")
        logging.info("assertTrue if alert message is displayed")

    def test_password_too_short_to_enter(self):
        """
        this function tests entering password that is too short (less than 6 characters).
        -----
        test case   #: 007
        requirement #: 003
        """
        logging.info("---------- Initialize Test: password too short (at least 6 characters) ----------")
        self.login_page.click_to_go_to_sign_up_button()
        self.sign_up_page = SignUpPage(self.driver)
        self.sign_up_page.enter_name_function(Utilities.generate_random_string_just_text(5))
        self.sign_up_page.enter_email_function(self.config["email_input"])
        self.sign_up_page.enter_and_re_enter_password_flow(Utilities.generate_random_string_just_numbers(4))
        self.sign_up_page.click_on_register_button()
        self.assertTrue(self.sign_up_page.check_if_sign_up_alert_message_is_displayed(),
                        "Error! Should NOT connect")
        logging.info("assertTrue if alert message is displayed")


if __name__ == '__main__':
    unittest.main()
