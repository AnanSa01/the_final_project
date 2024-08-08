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
        all_details = self.all_ratings.give_to_five_items_rating(self._api_request)

        print(f"\n{all_details}\n")


        api_get_products = Products(self._api_request)
        result_of_products = api_get_products.get_products_api()
        products = result_of_products.body["products"]

        all_details_updated = self.all_ratings.gather_all_details_for_items(all_details, products)
        print(all_details_updated)

        list_check_comment_true_ui = []
        list_check_rating_true_api = []
        for i in range(5):
            self.home_page.search_flow(all_details_updated[i][4])
            self.search_page = SearchPage(self.driver)
            self.search_page.click_on_first_result()
            self.product_page = ProductPage(self.driver)
            list_check_comment_true_ui.append(self.product_page.return_review_text() == all_details_updated[0][2])
            list_check_rating_true_api.append(products[all_details[i][3]] == all_details_updated[i][3])

            self.driver.refresh()



        # list_with_result_of_five_tests = self.all_ratings.check_all_ratings_for_item(self.driver, self.home_page,
        #                                                                              all_details_updated)
        print(list_check_comment_true_ui)
        print(list_check_rating_true_api)


        self.assertTrue(all(list_check_comment_true_ui))
        self.assertTrue(all(list_check_rating_true_api))

        # print()
        # print(all_details_updated)
        #
        # self.home_page.search_flow(all_details_updated[0][4])
        # self.search_page = SearchPage(self.driver)
        # self.search_page.click_on_first_result()
        # self.product_page = ProductPage(self.driver)
        # self.assertEqual(self.product_page.return_review_text(), all_details_updated[0][2])

        # for product in products:
        #     for i in range(5):
        #         if int(product["_id"]) == int(all_details[i][0]):
        #             all_details[i].append(product["name"])

        #print(all_true(my_list))


if __name__ == '__main__':
    unittest.main()
