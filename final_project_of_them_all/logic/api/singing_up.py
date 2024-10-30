from final_project_of_them_all.logic.api._base_init import BaseInit


class SigningUp(BaseInit):

    BASE_ENDPOINT_REGISTER = '/api/users/register/'

    def __init__(self, request):
        """
        All logic classes now share the same __init__ method by inheriting from a common base class.
        This refactor improves code efficiency by avoiding duplicate initialization code.

        :param request: The request object used to fetch API data.
        """
        super().__init__(request)

    def signing_up_api(self, payload):
        """
        this function returns given recommendations using GET
        """
        return self._request.post_request(f"{self.config["base_url"]}{self.BASE_ENDPOINT_REGISTER}",
                                             self.secret["header"], payload)
