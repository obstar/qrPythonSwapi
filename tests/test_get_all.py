import requests
from constants import Endpoint
from constants import StatusCode


def test_get_all_is_successful():
    response = requests.get(Endpoint.SWAPI_DEV_API)
    json_body = response.json()

    assert response.status_code == StatusCode.OK_200
    assert json_body['films'] == Endpoint.FILMS
    assert json_body['people'] == Endpoint.PEOPLE
    assert json_body['planets'] == Endpoint.PLANETS
    assert json_body['species'] == Endpoint.SPECIES
    assert json_body['starships'] == Endpoint.STARSHIPS
    assert json_body['vehicles'] == Endpoint.VEHICLES

def test_post_all_is_not_allowed():
    response = requests.post(Endpoint.SWAPI_DEV_API)
    assert response.status_code == StatusCode.METHOD_NOT_ALLOWED_405