from logic import utilities as UT


class SigningIn:
    def __init__(self, request):
        """
        all logic had the same __init__ , to make code more efficient I made them all inherent from the same page
        :param request: request to get API data
        """
        self._request = request
        self.config = UT.LoadCon.return_config()

    def signing_in_api(self, payload):
        """
        this function returns given recommendations using GET
        """
        return self._request.post_request(
            f"{self.config["base_url"]}/api/users/login/", self.config["header"], payload)
