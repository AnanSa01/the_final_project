from final_project_of_them_all.logic.utilities import LoadCon


class BaseInit:
    """
    `BaseInit` is the base class for all API logic, sharing common setup.

    Attributes:
        :param request: API request object accessible to all child classes.
        :param config: Configuration settings loaded from `LoadCon.return_config()`.
        :param secret: Sensitive data loaded from `LoadCon.return_secret()`.

    This class makes it easier to access shared resources, improving efficiency and maintenance.
    """
    def __init__(self, request):
        self._request = request
        self.config = LoadCon.return_config()
        self.secret = LoadCon.return_secret()
