import unittest
from infra.logging_basicConfig import LoggingSetup

from infra.api.api_wrapper import APIWrapper
from logic import utilities as UT
from logic.api.signing_in import SigningIn


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        request to get API data using APIWrapper, and load json file.
        """
        self._api_request = APIWrapper()
        self.config = UT.LoadCon.return_config()

    def tearDown(self):
        # logging.info(f'End of test.\n')
        ...

    def test_valid_login_api(self):
        """
        this function tests valid login with api
        -----
        test case   #: 013
        requirement #: 003
        """
        #logging.info("---------- Initialize Test: search employees (using GET) ----------")
        api_signing_in = SigningIn(self._api_request)
        payload_of_login = self.config["payload_for_login_api"]
        result_of_login = api_signing_in.signing_in_api(payload_of_login)
        self.assertEqual(result_of_login.status_code, 200)
        self.assertEqual(result_of_login.body["username"], self.config["email_input"])

    def test_invalid_login_api(self):
        """
        this function tests valid login with api
        -----
        test case   #: 013
        requirement #: 003
        """
        # logging.info("---------- Initialize Test: search employees (using GET) ----------")
        api_signing_in = SigningIn(self._api_request)
        payload_of_login = self.config["payload_for_invalid_login_api"]
        result_of_login = api_signing_in.signing_in_api(payload_of_login)
        self.assertEqual(result_of_login.status_code, 401)
        self.assertEqual(result_of_login.body["detail"], "No active account found with the given credentials")


if __name__ == '__main__':
    unittest.main()
