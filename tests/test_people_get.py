from constants import Endpoint
from constants import StatusCode

def test_people_get_is_successful(call):
    response = call.people.get()

    assert response.status_code == StatusCode.OK_200
    assert response.data['count'] == 82
    assert response.data['next'] == f'{Endpoint.PEOPLE}?page=2'
    assert response.data['results'] is not None

def test_people_post_is_not_allowed(call):
    response = call.people.get(method="POST")
    assert response.status_code == StatusCode.METHOD_NOT_ALLOWED_405