import unittest
from final_project_of_them_all.infra.api.api_wrapper import APIWrapper
from final_project_of_them_all.logic import utilities as UT
from final_project_of_them_all.logic.api.search_for_item import SearchForItem


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        Set up the test environment for API testing.

        Initializes the APIWrapper to handle API requests and loads configuration data from a JSON file.
        """
        self._api_request = APIWrapper()
        self.config = UT.LoadCon.return_config()

    def test_search_for_item_api(self):
        """
        Test case for searching an item via API.

        This test verifies that the API returns the correct product information when searching for a specific item.
        -----
        test case   #: 015
        requirement #: 004
        """
        api_search_for_item = SearchForItem(self._api_request)
        result_of_search_for_item = api_search_for_item.search_for_item_api()
        products = result_of_search_for_item.body["products"]
        self.assertEqual(result_of_search_for_item.status_code, 200)
        self.assertEqual(products[0]["name"], self.config["search_for_item"])





if __name__ == '__main__':
    unittest.main()
