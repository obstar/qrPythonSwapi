from api.calls.people import People
from api.calls.swapi import Swapi
from api.client import Client


class Call:
    def __init__(self):

        self.client = Client
        self.people = People(self)
        self.swapi = Swapi(self)

