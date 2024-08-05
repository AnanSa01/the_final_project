from logic import utilities as UT


class SearchForItem:
    def __init__(self, request):
        """
        all logic had the same __init__ , to make code more efficient I made them all inherent from the same page
        :param request: request to get API data
        """
        self._request = request
        self.config = UT.LoadCon.return_config()

    def search_for_item_api(self):
        """
        this function returns given recommendations using GET
        """
        return self._request.get_request(
            f"{self.config["base_url"]}/api/products/?keyword={self.config["search_for_item_encoded"]}", self.config["header"])
