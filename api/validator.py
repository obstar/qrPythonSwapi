import json
from types import SimpleNamespace
from requests import Response


class Validator:
    @staticmethod
    def structure(response: Response) -> Response:
        response.data = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))
        return response

    @staticmethod
    def return_endpoint_url(endpoint, params):
        if params is None:
            return f"{endpoint}"
        else:
            return f"{endpoint}{params}"
