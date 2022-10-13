from requests import Response
from api.validator import Validator
from constants import Endpoint, HttpMethod
from utils.logger import logging as log


class Swapi(Validator):
    def __init__(self, call):
        self.call = call

    @log("Get all for root")
    def get_all(self, method=HttpMethod.GET) -> Response:
        response = self.call.client.request(
            method = method,
            url=f"{Endpoint.SWAPI_DEV_API}",
        )
        return self.structure(response)