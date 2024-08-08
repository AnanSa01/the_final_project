import unittest

from final_project_of_them_all.infra.api.api_wrapper import APIWrapper
from final_project_of_them_all.logic.api.singing_up import SigningUp
from final_project_of_them_all.logic.utilities import LoadCon
from final_project_of_them_all.infra.utilities import Utilities as IUT


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        request to get API data using APIWrapper, and load json file.
        """
        self._api_request = APIWrapper()
        self.config = LoadCon.return_config()

    def tearDown(self):
        # logging.info(f'End of test.\n')
        ...

    def test_valid_sign_up_api(self):
        """
        this function tests valid login with api
        -----
        test case   #: 013
        requirement #: 003
        """
        #logging.info("---------- Initialize Test: search employees (using GET) ----------")
        api_signing_up = SigningUp(self._api_request)
        name = IUT.generate_random_string_just_text(8)
        email = IUT.generate_random_string_text_with_numbers(8) + self.config["emails_to_generate"]
        password = IUT.generate_random_string_just_numbers(8)
        payload_of_sign_up = {"name": name, "email": email, "password": password}
        result_of_sign_up = api_signing_up.signing_up_api(payload_of_sign_up)
        self.assertEqual(result_of_sign_up.status_code, 200)
        self.assertEqual(result_of_sign_up.body["username"], email)

    def test_negative_sign_up_with_already_signed_in_api(self):
        api_signing_up = SigningUp(self._api_request)
        payload_of_invalid_sign_up = self.config["payload_for_login_api"]
        result_of_sign_up = api_signing_up.signing_up_api(payload_of_invalid_sign_up)
        self.assertEqual(result_of_sign_up.status_code, 400)
        self.assertEqual(result_of_sign_up.body["detail"], "User with this email is already registered")


if __name__ == '__main__':
    unittest.main()
