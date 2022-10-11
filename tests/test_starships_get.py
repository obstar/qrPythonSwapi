from constants import Endpoint, TestData, ResponseError
from constants import StatusCode



def test_starships_get_all_is_successful(call):
    response = call.starships.get()
    assert response.status_code == StatusCode.OK_200
    assert response.data.count == 36
    assert response.data.next == f'{Endpoint.STARSHIPS}?page=2'
    assert response.data.previous is None
    assert response.data.results is not None


def test_starships_get_by_id_is_successful(call):
    response = call.starships.get(params="2/")
    assert response.status_code == StatusCode.OK_200
    assert response.data.name == TestData.CR_90_CORVETTE


def test_starships_post_is_not_allowed(call):
    response = call.starships.get(method="POST")
    assert response.status_code == StatusCode.METHOD_NOT_ALLOWED_405
    assert response.data.detail == ResponseError.METHOD_POST_NOT_ALLOWED
