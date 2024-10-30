from final_project_of_them_all.infra.config_provider import ConfigProvider
from final_project_of_them_all.logic.api._base_init import BaseInit
from final_project_of_them_all.logic.utilities import LoadCon


class AddRating(BaseInit):

    BASE_ENDPOINT_PRODUCT = "/api/products/"
    ENDPOINT_REVIEWS = "/reviews/"

    def __init__(self, request):
        """
        All logic classes now share the same __init__ method by inheriting from a common base class.
        This refactor improves code efficiency by avoiding duplicate initialization code.

        :param request: The request object used to fetch API data.
        """
        super().__init__(request)

    def add_rating_api(self, item_id, payload):
        """
        this function returns given recommendations using GET
        """
        return self._request.post_request(f"{self.config["base_url"]}{self.BASE_ENDPOINT_PRODUCT}{item_id}"
                                          f"{self.ENDPOINT_REVIEWS}", self.secret["header"], payload)
