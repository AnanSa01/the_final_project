from final_project_of_them_all.logic.utilities import LoadCon


class Products:
    def __init__(self, request):
        """
        Initialize the Products class with API request and configuration.

        :param request: API request object for making API calls
        """
        self._request = request
        self.config = LoadCon.return_config()

    def get_products_api(self):
        """
        Retrieve a list of products using a GET request.

        :return: Response object containing the list of products
        """
        return self._request.get_request(
            f"{self.config['base_url']}/api/products/", self.config["header"])