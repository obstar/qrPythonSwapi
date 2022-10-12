from api.calls.people import People
from api.calls.planets import Planets
from api.calls.starships import Starships
from api.calls.swapi import Swapi
from api.calls.vehicles import Vehicles
from api.client import Client
from api.validator import Validator
from utils.logger import logging as log
from requests import Response

class Call(Validator):
    def __init__(self):

        self.client = Client
        self.people = People(self)
        self.planets = Planets(self)
        self.starships = Starships(self)        
        self.swapi = Swapi(self)
        self.vehicles = Vehicles(self)   

    @log("Get by endpoint")
    @staticmethod
    def get_by_endpoint(self, url) -> Response:
        response = self.client.request(
            method = "GET",
            url = url,
        )
        return self.structure(response)