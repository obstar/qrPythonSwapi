from requests import Response
from api.validator import Validator
from constants import Endpoint
from common.logger import logging as log


class People(Validator):
    def __init__(self, app):
        self.app = app

    @log("Get for People endpoint")
    def get(self, method="GET") -> Response:
        response = self.app.client.request(
            method = method,
            url=f"{Endpoint.PEOPLE}",
        )
        return self.structure(response)