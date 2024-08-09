import unittest

from requests import JSONDecodeError

from final_project_of_them_all.infra.api.api_wrapper import APIWrapper
from final_project_of_them_all.infra.jira_handler import JiraHandler
from final_project_of_them_all.logic import utilities as UT
from final_project_of_them_all.logic.api.update_profile_information import UpdateProfileInformation


class MyTestCase(unittest.TestCase):
    def setUp(self):
        """
        request to get API data using APIWrapper, and load json file.
        """
        self._api_request = APIWrapper()
        self.config = UT.LoadCon.return_config()
        self.fail = True

    def tearDown(self):
        if self.fail:
            my_jira = JiraHandler()
            my_jira.create_issue('TEST', 'all good', 'i found a bug in this test')

    def test_search_for_item_api(self):
        api_update_profile_information = UpdateProfileInformation(self._api_request)
        payload = self.config["update_profile_information_payload"]
        result_update_profile_information = api_update_profile_information.update_profile_information_api(payload)
        self.assertTrue(result_update_profile_information.ok)
        self.assertEqual(result_update_profile_information.status_code, 200)
        self.fail = False


if __name__ == '__main__':
    unittest.main()
