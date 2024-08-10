import unittest

from final_project_of_them_all.infra.api.api_wrapper import APIWrapper
from final_project_of_them_all.logic.api.singing_up import SigningUp
from final_project_of_them_all.logic.utilities import LoadCon
from final_project_of_them_all.infra.utilities import Utilities as IUT


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment for API testing.

        Initializes the APIWrapper for handling API requests and loads configuration data from a JSON file.
        """
        self._api_request = APIWrapper()
        self.config = LoadCon.return_config()

    def tearDown(self):
        """
        Clean up after each test.

        Placeholder for any necessary cleanup tasks after tests. Currently, no operations are defined.
        """
        # logging.info(f'End of test.\n')
        ...

    def test_valid_sign_up_api(self):
        """
        Test case for valid sign-up via API.

        This test verifies that a user can successfully sign up with valid credentials through the API.
        -----
        test case   #: 003
        requirement #: 001
        """
        #logging.info("---------- Initialize Test: search employees (using GET) ----------")
        api_signing_up = SigningUp(self._api_request)
        name = IUT.generate_random_string_just_text(8)
        email = IUT.generate_random_string_text_with_numbers(8) + self.config["emails_to_generate"]
        password = IUT.generate_random_string_just_numbers(8)
        payload_of_sign_up = {"name": name, "email": email, "password": password}
        result_of_sign_up = api_signing_up.signing_up_api(payload_of_sign_up)
        self.assertEqual(result_of_sign_up.status_code, 200) # Check if the API response status code is 200
        self.assertEqual(result_of_sign_up.body["username"], email) # Verify that the returned username matches the provided email

    def test_negative_sign_up_with_already_signed_in_api(self):
        """
        Test case for sign-up attempt with an already registered email.

        This test ensures that the API returns an appropriate error message when attempting to sign up with an already registered email.
        -----
        test case   #: 008
        requirement #: 003
        """
        api_signing_up = SigningUp(self._api_request)
        payload_of_invalid_sign_up = self.config["payload_for_login_api"]
        result_of_sign_up = api_signing_up.signing_up_api(payload_of_invalid_sign_up)
        self.assertEqual(result_of_sign_up.status_code, 400)  # Check if the API response status code is 400
        self.assertEqual(result_of_sign_up.body["detail"], "User with this email is already registered")


if __name__ == '__main__':
    unittest.main()
