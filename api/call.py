from api.calls.people import People
from api.calls.swapi import Swapi
from api.client import Client
from api.validator import Validator
from common.logger import logging as log
from requests import Response

class Call(Validator):
    def __init__(self):

        self.client = Client
        self.people = People(self)
        self.swapi = Swapi(self)

    @log("Get by endpoint")
    @staticmethod
    def get_by_endpoint(self, url) -> Response:
        response = self.client.request(
            method = "GET",
            url = url,
        )
        return self.structure(response)