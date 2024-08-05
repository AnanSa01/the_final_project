from final_project_of_them_all.infra.config_provider import ConfigProvider


class AddRating:
    def __init__(self, request):
        """
        all logic had the same __init__ , to make code more efficient I made them all inherent from the same page
        :param request: request to get API data
        """
        self._request = request
        self.config = ConfigProvider.load_from_file('../config.json')

    def add_rating_api(self):
        """
        this function returns given recommendations using GET
        """
        return self._request.post_request(f"{self.config["base_url"]}/api/products/{self.config["add_rating_item"]}", self.config["header"], self.config["payload_for_poc"])
