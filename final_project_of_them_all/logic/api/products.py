from final_project_of_them_all.logic.utilities import LoadCon


class Products:
    def __init__(self, request):
        """
        all logic had the same __init__ , to make code more efficient I made them all inherent from the same page
        :param request: request to get API data
        """
        self._request = request
        self.config = LoadCon.return_config()

    def get_products_api(self):
        """
        this function returns given recommendations using GET
        """
        return self._request.get_request(
            f"{self.config["base_url"]}/api/products/", self.config["header"])
