from constants import Endpoint, TestData, ResponseError
from constants import StatusCode



def test_vehicles_get_all_is_successful(call):
    response = call.vehicles.get()
    assert response.status_code == StatusCode.OK_200
    assert response.data.count == 39
    assert response.data.next == f'{Endpoint.VEHICLES}?page=2'
    assert response.data.previous is None
    assert response.data.results is not None


def test_vehicles_get_by_id_is_successful(call):
    response = call.vehicles.get(params="4/")
    assert response.status_code == StatusCode.OK_200
    assert response.data.name == TestData.SAND_CRAWLER


def test_vehicles_post_is_not_allowed(call):
    response = call.vehicles.get(method="POST")
    assert response.status_code == StatusCode.METHOD_NOT_ALLOWED_405
    assert response.data.detail == ResponseError.METHOD_POST_NOT_ALLOWED
