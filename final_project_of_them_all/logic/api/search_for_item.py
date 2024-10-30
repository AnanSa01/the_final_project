from final_project_of_them_all.logic.api._base_init import BaseInit
from final_project_of_them_all.logic.utilities import LoadCon


class SearchForItem(BaseInit):

    BASE_ENDPOINT_PRODUCTS = '/api/products/'
    PARAM_KEYWORD = '?keyword='

    def __init__(self, request):
        """
        All logic classes now share the same __init__ method by inheriting from a common base class.
        This refactor improves code efficiency by avoiding duplicate initialization code.

        :param request: The request object used to fetch API data.
        """
        super().__init__(request)

    def search_for_item_api(self):
        """
        this function returns given recommendations using GET
        """
        return self._request.get_request(f"{self.config["base_url"]}{self.BASE_ENDPOINT_PRODUCTS}{self.PARAM_KEYWORD}"
                                         f"{self.config["search_for_item_encoded"]}", self.secret["header"])
