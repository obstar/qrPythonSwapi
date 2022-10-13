from requests import Response
from api.validator import Validator
from constants import Endpoint, HttpMethod
from utils.logger import logging as log


class Planets(Validator):
    def __init__(self, call):
        self.call = call

    @log("Get for Planets endpoint")
    def get(self, method=HttpMethod.GET, params=None, is_json=True) -> Response:
        response = self.call.client.request(
            method = method,
            url = self.return_endpoint_url(Endpoint.PLANETS, params),
        )
        if is_json: return self.structure(response)
        else: return response
