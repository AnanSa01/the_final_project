import random

from selenium.webdriver.common.by import By
from final_project_of_them_all.infra.utilities import Utilities as IUT
from final_project_of_them_all.logic.api.add_rating import AddRating
from final_project_of_them_all.logic.ui.base_page_app import BasePageApp
from final_project_of_them_all.logic.ui.home_page import HomePage
from final_project_of_them_all.logic.ui.product_page import ProductPage
from final_project_of_them_all.logic.ui.search_page import SearchPage


class AllRatings(BasePageApp):
    ITEM_TITLE = '//div[@class="card-body"]//a'

    def give_to_five_items_rating(self, request):
        self._all_items = self._driver.find_elements(By.XPATH, self.ITEM_TITLE)
        already_selected_items = []
        all_details = []
        for i in range(5):
            item = random.randint(1, 7)
            while item in already_selected_items:
                item = random.randint(1, 7)
            already_selected_items.append(item)
            attribute_value = self._all_items[item].get_attribute("href").split("/")
            print(f"id= {attribute_value[5]}")
            item_id = attribute_value[5]
            item_index = item

            rating = i + 1
            print(f"rating= {rating}")

            comment = IUT.generate_random_string_just_text(6)
            print(f"comment= {comment}")

            payload = {"rating": rating, "comment": comment}
            print(f"payload= {payload}\n\n")

            api_rate_one = AddRating(request)
            api_rate_one.add_rating_api(item_id, payload)

            id_and_reviews = [item_id, rating, comment, item_index]

            all_details.append(id_and_reviews)


        return all_details

    def gather_all_details_for_items(self, all_details, products):

        for product in products:
            for i in range(5):
                if int(product["_id"]) == int(all_details[i][0]):
                    all_details[i].append(product["name"])

        return all_details

    def check_all_ratings_for_item(self, driver, home_page, all_details_updated):
        list_check_true = []
        for i in range(5):
            home_page.search_flow(all_details_updated[i][4])
            self.search_page = SearchPage(driver)
            self.search_page.click_on_first_result()
            self.product_page = ProductPage(driver)
            list_check_true.append(self.product_page.return_review_text() == all_details_updated[0][2])
            driver.close()

        return list_check_true