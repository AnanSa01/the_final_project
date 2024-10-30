import logging
import random

from selenium.webdriver.common.by import By
from final_project_of_them_all.infra.utilities import Utilities as IUT
from final_project_of_them_all.logic.api.add_review import AddRating
from final_project_of_them_all.logic.ui.base_page_app import BasePageApp
from final_project_of_them_all.logic.ui.home_page import HomePage
from final_project_of_them_all.logic.ui.product_page import ProductPage
from final_project_of_them_all.logic.ui.search_page import SearchPage
from final_project_of_them_all.logic.utilities import LoadJSON


class AllRatings(BasePageApp):
    ITEM_TITLE = '//div[@class="card-body"]//a'

    def give_to_five_items_rating(self, request):
        """
        Rates five random items with unique ratings and comments.

        :param request: API request object for adding ratings.
        :return: List of details for the rated items including ID, rating, comment, and index.
        """
        # Find all item elements on the page
        self._all_items = self._driver.find_elements(By.XPATH, self.ITEM_TITLE)
        self.config = LoadJSON.return_config()
        already_selected_items = []
        all_details = []

        for i in range(self.config["in_range"]):
            # Select only unique random items
            item = random.randint(self.config["random_from"], len(self._all_items) - 1)
            while item in already_selected_items:
                item = random.randint(self.config["random_from"], len(self._all_items) - 1)
            already_selected_items.append(item)

            # Extract item ID from UI
            attribute_value = self._all_items[item].get_attribute("href").split("/")
            item_id = attribute_value[self.config["id_split"]]
            item_index = item

            # Generate rating and comment
            rating = i + 1
            comment = IUT.generate_random_string_just_text(6)

            # Prepare payload for API request
            payload = {"rating": rating, "comment": comment}

            try:
                # Send API request to add rating with ID and payload we prepared from last line.
                api_rate_one = AddRating(request)
                api_rate_one.add_rating_api(item_id, payload)
            except Exception:
                logging.error(f"Failed to rate item {item_id}")

            # Store details of the rated item in a list.
            # Name attribute is unavailable here. To include it,
            # an additional API request to the "Products" endpoint is required.
            id_and_reviews = {"id": item_id, "rating": rating, "comment": comment,
                              "index": item_index, "name_item": None}
            all_details.append(id_and_reviews)

        return all_details

    def gather_all_details_for_items(self, all_details, products):
        """
        Adds product names to the details of rated items.

        :param all_details: List of item details including ID, rating, comment, and index.
        :param products: List of product data including IDs and names.
        :return: Updated list of item details with product names.
        """
        for product in products:
            for i in range(self.config["in_range"]):
                if int(product["_id"]) == int(all_details[i]["id"]):
                    all_details[i]["name_item"] = product["name"]

        return all_details

    def check_all_ratings_for_item(self, driver, all_details_updated):
        """
        Verifies that the ratings and comments for items are correctly displayed on the product pages.

        :param driver: Selenium WebDriver instance.
        :param all_details_updated: List of updated item details with product names.
        :return: List of boolean values indicating whether the ratings and comments are correctly displayed.
        """
        list_check_true = []

        self.search_page = SearchPage(driver)
        self.product_page = ProductPage(driver)

        for i in range(self.config["in_range"]):
            # Search for the product and check if the review text matches
            self.search_flow(all_details_updated[i]["name_item"])
            self.search_page.click_on_first_result()

            # Check if each comment from API request IS IN the comment section from UI, and append TRUE/FALSE to list.
            list_check_true.append(all_details_updated[i]["comment"] in self.product_page.return_review_text())
            # Refresh the page to clear the search bar for entering a new search term.
            self.refresh_page()

        return list_check_true

    def get_false_details(self, all_details, list_results):
        """
        Identifies and returns details of items with incorrect ratings or comments.

        :param all_details: List of item details including ID, rating, comment, and index.
        :param list_results: List of boolean values indicating whether the ratings and comments are correctly displayed.
        :return: List of dictionaries containing names of items with incorrect results.
        """
        false_list = []
        for i, result in enumerate(list_results):
            if not result:
                false_list.append({"False": [all_details[i]["id"], all_details[i]["name_item"]]})

        return false_list
