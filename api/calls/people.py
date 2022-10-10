from requests import Response
from api.validator import Validator
from constants import Endpoint
from common.logger import logging as log


class People(Validator):
    def __init__(self, app):
        self.app = app

    @log("Get for People endpoint")
    def get(self, method="GET", params=None) -> Response:
        response = self.app.client.request(
            method = method,
            url = self.return_endpoint_url(Endpoint.PEOPLE, params),
        )
        return self.structure(response)