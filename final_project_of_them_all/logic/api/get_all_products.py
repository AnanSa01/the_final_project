from final_project_of_them_all.logic.api._base_init_for_api import BaseInit


class Products(BaseInit):
    BASE_ENDPOINT_PRODUCTS = "/api/products/"

    def __init__(self, request):
        """
        All logic classes now share the same __init__ method by inheriting from a common base class.
        This refactor improves code efficiency by avoiding duplicate initialization code.

        :param request: The request object used to fetch API data.
        """
        super().__init__(request)

    def get_products_api(self):
        """
        Retrieve a list of products using a GET request.

        :return: Response object containing the list of products
        """
        return self._request.get_request(f"{self.config['base_url']}{self.BASE_ENDPOINT_PRODUCTS}",
                                         self.secret["header"])
