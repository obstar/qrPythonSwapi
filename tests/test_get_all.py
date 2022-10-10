from constants import Endpoint, ResponseError
from constants import StatusCode


def test_get_all_is_successful(call):
    response = call.swapi.get_all()

    assert response.status_code == StatusCode.OK_200
    assert response.data['films'] == Endpoint.FILMS
    assert response.data['people'] == Endpoint.PEOPLE
    assert response.data['planets'] == Endpoint.PLANETS
    assert response.data['species'] == Endpoint.SPECIES
    assert response.data['starships'] == Endpoint.STARSHIPS
    assert response.data['vehicles'] == Endpoint.VEHICLES

def test_post_all_is_not_allowed(call):
    response = call.swapi.get_all(method="POST")
    assert response.status_code == StatusCode.METHOD_NOT_ALLOWED_405
    assert response.data['detail'] == ResponseError.METHOD_POST_NOT_ALLOWED