import unittest
from infra.api.api_wrapper import APIWrapper
from logic import utilities as UT
from logic.api.search_for_item import SearchForItem


class MyTestCase(unittest.TestCase):

    def setUp(self):
        """
        request to get API data using APIWrapper, and load json file.
        """
        self._api_request = APIWrapper()
        self.config = UT.LoadCon.return_config()

    def test_search_for_item_api(self):
        api_search_for_item = SearchForItem(self._api_request)
        result_of_search_for_item = api_search_for_item.search_for_item_api()
        products = result_of_search_for_item.body["products"]
        self.assertEqual(result_of_search_for_item.status_code, 200)
        self.assertEqual(products[0]["name"], self.config["search_for_item"])





if __name__ == '__main__':
    unittest.main()
