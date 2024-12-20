import logging
import unittest

from final_project_of_them_all.infra.api.api_wrapper import APIWrapper
from final_project_of_them_all.logic.api.singing_up import SigningUp
from final_project_of_them_all.logic.utilities import LoadJSON
from final_project_of_them_all.infra.utilities import Utilities as IUT


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment for API testing.

        Initializes the APIWrapper for handling API requests and loads configuration data from a JSON file.
        """
        self._api_request = APIWrapper()
        self.config = LoadJSON.return_config()

    def tearDown(self):
        """
        Clean up after each test.

        Placeholder for any necessary cleanup tasks after tests. Currently, no operations are defined.
        """
        logging.info(f'End of test.\n')

    def test_valid_sign_up_api(self):
        """
        Test case for valid sign-up via API.

        This test verifies that a user can successfully sign up with valid credentials through the API.
        -----
        test case   #: 003
        requirement #: 001
        """
        logging.info("Initialize Test: valid sign up with API")

        api_signing_up = SigningUp(self._api_request)
        name = IUT.generate_random_string_just_text(self.config["generated_numbers"])
        email = (IUT.generate_random_string_text_with_numbers(self.config["generated_numbers"]) +
                 self.config["emails_to_generate"])
        password = IUT.generate_random_string_just_numbers(self.config["generated_numbers"])
        payload_of_sign_up = {"name": name, "email": email, "password": password}
        result_of_sign_up = api_signing_up.signing_up_api(payload_of_sign_up)
        self.assertEqual(result_of_sign_up.status_code, self.config["success_response"])
        self.assertEqual(result_of_sign_up.body["username"], email)

    def test_negative_sign_up_with_already_signed_in_api(self):
        """
        Test case for sign-up attempt with an already registered email.

        This test ensures that the API returns an appropriate error message when attempting to sign up with an already registered email.
        -----
        test case   #: 008
        requirement #: 003
        """
        logging.info("Initialize Test: invalid sign up with API")

        api_signing_up = SigningUp(self._api_request)
        payload_of_invalid_sign_up = self.config["payload_for_login_api"]
        result_of_sign_up = api_signing_up.signing_up_api(payload_of_invalid_sign_up)
        self.assertEqual(result_of_sign_up.status_code,
                         self.config["response_not_found"])  # Check if the API response status code is 400
        self.assertEqual(result_of_sign_up.body["detail"], self.config["message_invalid_sign_up"])


if __name__ == '__main__':
    unittest.main()
