from constants import TestData, StatusCode



def test_vehicles_get_search_is_successful(call):
    """
    1. Query vehicles to get CR90 corvette data
    2. Validate response data
    3. Loop through films
    4. For each film endpoint assert that status code is 200 OK 
    5. Assert that searched vehicle is on the vehicles list of the validated film
    """
    response_cr90_corvette = call.vehicles.get(params=f"?search={TestData.SAND_CRAWLER}")
    assert response_cr90_corvette.status_code == StatusCode.OK_200
    assert response_cr90_corvette.data.count == 1
    assert response_cr90_corvette.data.results[0].name == TestData.SAND_CRAWLER

    for film in response_cr90_corvette.data.results[0].films:
        response_film = call.get_by_endpoint(film)
        assert response_film.status_code == StatusCode.OK_200
        assert response_cr90_corvette.data.results[0].url in response_film.data.vehicles


def test_vehicles_get_search_uri_is_too_large(call):
    response = call.vehicles.get(params=f"?search={TestData.TOO_LARGE}", is_json=False)
    assert response.status_code == StatusCode.REQUEST_URI_TOO_LARGE_414
