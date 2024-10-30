import logging
import unittest

from final_project_of_them_all.infra.logging_basicConfig import LoggingSetup
from final_project_of_them_all.infra.ui.browser_wrapper import BrowserWrapper
from final_project_of_them_all.logic.ui.home_page import HomePage
from final_project_of_them_all.logic.utilities import LoadJSON
from final_project_of_them_all.infra.utilities import Utilities
from final_project_of_them_all.logic.ui.login_page import LoginPage
from final_project_of_them_all.logic.ui.sign_up_page import SignUpPage


class MyTestCase(unittest.TestCase):
    """
    Test suite for verifying user login and sign-up functionalities.

    Tests include:
    - Valid login
    - Login with missing password
    - Login with missing email and password
    - Sign-up with an already registered email
    - Sign-up with invalid email format
    - Sign-up with mismatched passwords
    - Sign-up with a password that is too short
    """

    def setUp(self):
        """
        Set up the test environment.

        Initializes the browser, loads configuration, and sets up the login page.
        """
        # ARRANGE
        self.browser = BrowserWrapper()
        self.config = LoadJSON.return_config()
        self.driver = self.browser.get_driver(self.config["base_url_login"])
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        """
        Clean up after each test.

        Closes the browser and logs the completion of the test.
        """
        self.driver.close()
        logging.info(f'End of test. {self.config["browser"]} web driver is closed.\n')

    def test_valid_login(self):
        """
        Test case for valid login input.

        This test verifies that a user can successfully log in with valid credentials.
        -----
        test case   #: 001
        requirement #: 001
        """
        logging.info("Initialize Test: valid login with UI")

        # ACT
        self.login_page.write_in_email_input_field(self.config["email_input"])
        self.login_page.write_in_password_input_field(self.config["password_input"])
        self.login_page.click_on_sign_in_button()
        self.home_page = HomePage(self.driver)

        # ASSERT
        success_message = self.home_page.return_displayed_successful_login_message()
        self.assertTrue(success_message)

    def test_not_adding_password_in_login(self):
        """
        Test case for login attempt without providing a password.

        This test ensures that the system does not log in when the password field is empty.
        -----
        test case   #: 004
        requirement #: 002
        """
        logging.info("Initialize Test: not adding password in login with UI")

        # ACT
        self.login_page.write_in_email_input_field(self.config["email_input"])
        self.login_page.click_on_sign_in_button()

        # ASSERT
        alert_displayed = self.login_page.check_if_login_alert_message_is_displayed()
        self.assertTrue(alert_displayed)

    def test_not_adding_password_nor_email_in_login(self):
        """
        Test case for login attempt without providing email and password.

        This test ensures that the system does not log in when both email and password fields are empty.
        -----
        test case   #: 005
        requirement #: 002
        """
        logging.info("Initialize Test: not adding password nor email in login with UI")

        # ACT
        self.login_page.click_on_sign_in_button()

        # ASSERT
        alert_displayed = self.login_page.check_if_login_alert_message_is_displayed()
        self.assertTrue(alert_displayed)

    def test_sign_up_with_already_connected_user(self):
        """
        Test case for sign-up with an already registered email.

        This test verifies that the system does not allow a user to sign up with an email that is already registered.
        -----
        test case   #: 007
        requirement #: 003
        """
        logging.info("Initialize Test: signing up with already connected user with UI")

        # ACT
        self.login_page.click_to_go_to_sign_up_button()
        self.sign_up_page = SignUpPage(self.driver)
        self.sign_up_page.enter_name_function(self.config["name_input"])
        self.sign_up_page.enter_email_function(self.config["email_input"])
        self.sign_up_page.enter_and_re_enter_password_flow(self.config["password_input"])
        self.sign_up_page.click_on_register_button()

        # ASSERT
        alert_displayed = self.sign_up_page.check_if_sign_up_alert_message_is_displayed()
        self.assertTrue(alert_displayed)

    def test_invalid_email_sign_up(self):
        """
        Test case for sign-up with an invalid email format.

        This test ensures that the system does not allow sign-up with an invalid email format.
        -----
        test case   #: 009
        requirement #: 003
        """
        logging.info("Initialize Test: invalid email sign-up with UI")

        # ACT
        self.login_page.click_to_go_to_sign_up_button()
        self.sign_up_page = SignUpPage(self.driver)
        self.sign_up_page.enter_name_function(Utilities.generate_random_string_just_text(5))
        self.sign_up_page.enter_email_function(Utilities.generate_random_string_just_punctuation(10))
        self.sign_up_page.enter_and_re_enter_password_flow(Utilities.generate_random_string_just_numbers(8))
        self.sign_up_page.click_on_register_button()

        # ASSERT
        still_on_register_page = self.sign_up_page.check_if_still_on_register_page()
        self.assertTrue(still_on_register_page)

    def test_password_not_match_re_enter_password(self):
        """
        Test case for sign-up with mismatched passwords.

        This test verifies that the system does not allow sign-up when the password and re-entered password do not match.
        -----
        test case   #: 010
        requirement #: 003
        """
        logging.info("Initialize Test: password not matching re-entering password with UI")

        # ACT
        self.login_page.click_to_go_to_sign_up_button()
        self.sign_up_page = SignUpPage(self.driver)
        self.sign_up_page.enter_name_function(Utilities.generate_random_string_just_text(5))
        self.sign_up_page.enter_email_function(self.config["email_input"])
        self.sign_up_page.enter_password_function(Utilities.generate_random_string_just_numbers(8))
        self.sign_up_page.re_enter_password_function(Utilities.generate_random_string_just_numbers(9))
        self.sign_up_page.click_on_register_button()

        # ASSERT
        alert_displayed = self.sign_up_page.check_if_sign_up_alert_message_is_displayed()
        self.assertTrue(alert_displayed)

    def test_password_too_short_to_enter(self):
        """
        Test case for sign-up with a password that is too short.

        This test ensures that the system does not allow sign-up with a password shorter than the minimum required length.
        -----
        test case   #: 011
        requirement #: 003
        """
        logging.info("Initialize Test: password too short (at least 6 characters) with UI")

        # ACT
        self.login_page.click_to_go_to_sign_up_button()
        self.sign_up_page = SignUpPage(self.driver)
        self.sign_up_page.enter_name_function(Utilities.generate_random_string_just_text(5))
        self.sign_up_page.enter_email_function(self.config["email_input"])
        self.sign_up_page.enter_and_re_enter_password_flow(Utilities.generate_random_string_just_numbers(4))
        self.sign_up_page.click_on_register_button()

        # ASSERT
        alert_displayed = self.sign_up_page.check_if_sign_up_alert_message_is_displayed()
        self.assertTrue(alert_displayed)


if __name__ == '__main__':
    unittest.main()
