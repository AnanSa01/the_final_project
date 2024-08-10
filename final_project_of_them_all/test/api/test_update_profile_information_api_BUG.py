import unittest

from requests import JSONDecodeError

from final_project_of_them_all.infra.api.api_wrapper import APIWrapper
from final_project_of_them_all.infra.jira_handler import JiraHandler
from final_project_of_them_all.logic import utilities as UT
from final_project_of_them_all.logic.api.update_profile_information import UpdateProfileInformation


class MyTestCase(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment for API testing.

        Initializes the API wrapper and loads configuration data.
        """
        self._api_request = APIWrapper()
        self.config = UT.LoadCon.return_config()
        self.fail = True

    def tearDown(self):
        """
        Clean up after tests.

        If the test failed, create a Jira issue to report the problem.
        """
        if self.fail:
            my_jira = JiraHandler()
            my_jira.create_issue('TEST', 'all good', 'i found a bug in this test')

    def test_search_for_item_api(self):
        """
        Test case for updating profile information through the API.

        This test checks the behavior of the `update_profile_information` API endpoint.
        -----
        test case   #: 025
        requirement #: 014
        """
        # Initialize API wrapper and define payload
        api_update_profile_information = UpdateProfileInformation(self._api_request)
        payload = self.config["update_profile_information_payload"]

        # Make the API request to update profile information
        result_update_profile_information = api_update_profile_information.update_profile_information_api(payload)

        # Assert that the request was successful
        self.assertTrue(result_update_profile_information.ok)
        self.assertEqual(result_update_profile_information.status_code, 200)

        # If assertions pass, set fail to False
        self.fail = False


if __name__ == '__main__':
    unittest.main()
