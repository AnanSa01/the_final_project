from final_project_of_them_all.infra.config_provider import ConfigProvider
from final_project_of_them_all.logic.utilities import LoadCon


class AddRating:
    def __init__(self, request):
        """
        all logic had the same __init__ , to make code more efficient I made them all inherent from the same page
        :param request: request to get API data
        """
        self._request = request
        self.config = LoadCon.return_config()
        self.secret = LoadCon.return_secret()

    def add_rating_api(self, item_id, payload):
        """
        this function returns given recommendations using GET
        """
        return self._request.post_request(f"{self.config["base_url"]}/api/products/{item_id}/reviews/",
                                             self.secret["header"], payload)
