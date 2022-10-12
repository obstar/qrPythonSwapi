from requests import Response
from api.validator import Validator
from constants import Endpoint
from utils.logger import logging as log


class People(Validator):
    def __init__(self, call):
        self.call = call

    @log("Get for People endpoint")
    def get(self, method="GET", params=None, is_json=True) -> Response:
        response = self.call.client.request(
            method = method,
            url = self.return_endpoint_url(Endpoint.PEOPLE, params),
        )
        if is_json: return self.structure(response)
        else: return response
