import requests

from final_project_of_them_all.infra.api.response_wrapper import ResponseWrapper


class APIWrapper:
    """
    using "requests" package to use API data in many functions
    """

    def __init__(self):
        self._request = None

    @staticmethod
    def get_request(url, headers=None, payload=None):
        response = requests.get(url, headers=headers, json=payload)
        return ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response)

    @staticmethod
    def post_request(url, headers=None, payload=None):
        response = requests.post(url, headers=headers, json=payload)
        return ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response)

    @staticmethod
    def put_request(url, headers=None, payload=None):
        response = requests.put(url, headers=headers, json=payload)
        return ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response)
