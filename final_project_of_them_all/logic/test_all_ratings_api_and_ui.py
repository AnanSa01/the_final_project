import random

from selenium.webdriver.common.by import By
from final_project_of_them_all.infra.utilities import Utilities as IUT
from final_project_of_them_all.logic.api.add_rating import AddRating
from final_project_of_them_all.logic.ui.base_page_app import BasePageApp


class AllRatings(BasePageApp):
    ITEM_TITLE = '//div[@class="card-body"]//a'

    def manage_rating(self, request):
        self._all_items = self._driver.find_elements(By.XPATH, self.ITEM_TITLE)
        already_selected_items = []
        item_id_and_reviews = []
        for i in range(5):
            item = random.randint(1, 7)
            while item in already_selected_items:
                item = random.randint(1, 7)
            already_selected_items.append(item)
            attribute_value = self._all_items[item].get_attribute("href").split("/")
            print(f"id= {attribute_value[5]}")
            item_id = attribute_value[5]

            rating = i + 1
            print(f"rating= {rating}")

            comment = IUT.generate_random_string_just_text(6)
            print(f"comment= {comment}")

            payload = {"rating": rating, "comment": comment}
            print(f"payload= {payload}\n\n")

            api_rate_one = AddRating(request)
            api_rate_one.add_rating_api(item_id, payload)

            rating_and_comment = [rating, comment]

            item_id_and_reviews.append({item_id: rating_and_comment})


        print(already_selected_items)
        print(item_id_and_reviews)
        return item_id_and_reviews