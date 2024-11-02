class ResponseWrapper:
    def __init__(self, ok, status_code, body):
        self.ok = ok
        self.status_code = status_code
        self.body = self._check_body(body)

    @staticmethod
    def _check_body(body):
        try:
            return body.json()
        except ValueError:
            return body.text
