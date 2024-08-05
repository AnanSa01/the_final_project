import requests

from infra.api.response_wrapper import ResponseWrapper


class APIWrapper:
    """
    using "requests" package to use API data in many functions
    """

    def __init__(self):
        self._request = None

    @staticmethod
    def get_request(url, headers=None, body=None):
        response = requests.get(url, headers=headers, json=body)
        return ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response.json())

    @staticmethod
    def post_request(url, headers=None, body=None):
        response = requests.post(url, headers=headers, json=body)
        return ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response.json())
