from constants import Endpoint, TestData, ResponseError
from constants import StatusCode



def test_planets_get_all_is_successful(call):
    response = call.planets.get()
    assert response.status_code == StatusCode.OK_200
    assert response.data.count == 60
    assert response.data.next == f'{Endpoint.PLANETS}?page=2'
    assert response.data.previous is None
    assert response.data.results is not None


def test_planets_get_by_id_is_successful(call):
    response = call.planets.get(params="1/")
    assert response.status_code == StatusCode.OK_200
    assert response.data.name == TestData.TATOOINE


def test_planets_post_is_not_allowed(call):
    response = call.planets.get(method="POST")
    assert response.status_code == StatusCode.METHOD_NOT_ALLOWED_405
    assert response.data.detail == ResponseError.METHOD_POST_NOT_ALLOWED
