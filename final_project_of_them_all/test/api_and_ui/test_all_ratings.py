import unittest
from final_project_of_them_all.infra.api.api_wrapper import APIWrapper
from final_project_of_them_all.infra.ui.browser_wrapper import BrowserWrapper
from final_project_of_them_all.logic.api.add_rating import AddRating
from final_project_of_them_all.logic.api.products import Products
from final_project_of_them_all.logic.test_all_ratings_api_and_ui import AllRatings
from final_project_of_them_all.logic.ui.home_page import HomePage
from final_project_of_them_all.logic.ui.login_page import LoginPage
from final_project_of_them_all.logic.utilities import LoadCon


class MyTestCase(unittest.TestCase):

    def test_all_ratings(self):
        self._api_request = APIWrapper()

        self.config = LoadCon.return_config()
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.browser.config["base_url_login"])
        self.login_page = LoginPage(self.driver)
        self.login_page.write_in_email_input_field(self.config["email_input"])
        self.login_page.write_in_password_input_field(self.config["password_input"])
        self.login_page.click_on_sign_in_button()
        self.home_page = HomePage(self.driver)
        self.all_ratings = AllRatings(self.driver)
        id_and_payload = self.all_ratings.manage_rating(self._api_request)

        print(id_and_payload)

        # api_rate_one = AddRating(self._api_request)
        # api_rate_one.add_rating_api(id_and_payload[0], id_and_payload[1])
        #
        # print(result_of_all_ratings.body)


        # api_all_ratings = AddRating(request)
        # return api_all_ratings.add_rating_api(item_id, payload)

        api_get_products = Products(self._api_request)
        result_of_products = api_get_products.get_products_api()
        print(result_of_products.body)
        products = result_of_products.body["products"]





if __name__ == '__main__':
    unittest.main()
