from requests import Response
from api.validator import Validator
from constants import Endpoint
from common.logger import logging as log


class Swapi(Validator):
    def __init__(self, app):
        self.app = app

    @log("Get all for root")
    def get_all(self, method="GET") -> Response:
        response = self.app.client.request(
            method = method,
            url=f"{Endpoint.SWAPI_DEV_API}",
        )
        return self.structure(response)