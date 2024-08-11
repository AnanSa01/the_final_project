import unittest

from final_project_of_them_all.infra.api.api_wrapper import APIWrapper
from final_project_of_them_all.logic import utilities as UT
from final_project_of_them_all.logic.api.login import SigningIn


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment for API testing.

        Initializes the APIWrapper to handle API requests and loads configuration data from a JSON file.
        """
        self._api_request = APIWrapper()
        self.config = UT.LoadCon.return_config()

    def tearDown(self):
        """
        Clean up after each test.

        Placeholder for any cleanup tasks after tests. Currently, no operations are defined.
        """
        # logging.info(f'End of test.\n')
        ...

    def test_valid_login_api(self):
        """
        Test case for valid login via API.

        This test verifies that a user can successfully log in with valid credentials through the API.
        -----
        test case   #: 002
        requirement #: 001
        """
        #logging.info("---------- Initialize Test: search employees (using GET) ----------")
        api_signing_in = SigningIn(self._api_request)
        payload_of_login = self.config["payload_for_login_api"]
        result_of_login = api_signing_in.signing_in_api(payload_of_login)
        self.assertEqual(result_of_login.status_code, self.config["success_response"])
        self.assertEqual(result_of_login.body["username"], self.config["email_input"])

    def test_invalid_login_api(self):
        """
        Test case for invalid login via API.

        This test ensures that the API returns an appropriate error message when attempting to log in with invalid credentials.
        -----
        test case   #: 006
        requirement #: 001
        """
        # logging.info("---------- Initialize Test: search employees (using GET) ----------")
        api_signing_in = SigningIn(self._api_request)
        payload_of_login = self.config["payload_for_invalid_login_api"]
        result_of_login = api_signing_in.signing_in_api(payload_of_login)
        self.assertEqual(result_of_login.status_code, self.config["response_not_active"])
        self.assertEqual(result_of_login.body["detail"], "No active account found with the given credentials")
        print(result_of_login.body)


if __name__ == '__main__':
    unittest.main()
