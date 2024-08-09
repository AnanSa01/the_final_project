import unittest
from final_project_of_them_all.infra.api.api_wrapper import APIWrapper
from final_project_of_them_all.infra.ui.browser_wrapper import BrowserWrapper
from final_project_of_them_all.logic.api.add_rating import AddRating
from final_project_of_them_all.logic.api.products import Products
from final_project_of_them_all.logic.test_all_ratings_api_and_ui import AllRatings
from final_project_of_them_all.logic.ui.home_page import HomePage
from final_project_of_them_all.logic.ui.login_page import LoginPage
from final_project_of_them_all.logic.ui.product_page import ProductPage
from final_project_of_them_all.logic.ui.search_page import SearchPage
from final_project_of_them_all.logic.utilities import LoadCon


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self._api_request = APIWrapper()

        self.config = LoadCon.return_config()
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.config["base_url_login"])
        self.login_page = LoginPage(self.driver)
        self.login_page.login_flow(self.config["email_input"], self.config["password_input"])
        self.home_page = HomePage(self.driver)

    def test_all_ratings(self):
        self.all_ratings = AllRatings(self.driver)
        all_details = self.all_ratings.give_to_five_items_rating(self._api_request)
        api_get_products = Products(self._api_request)
        result_of_products = api_get_products.get_products_api()
        products = result_of_products.body["products"]
        all_details_updated = self.all_ratings.gather_all_details_for_items(all_details, products)
        list_with_result_of_five_tests = self.all_ratings.check_all_ratings_for_item(self.driver, all_details_updated)
        self.assertTrue(all(list_with_result_of_five_tests))


if __name__ == '__main__':
    unittest.main()
