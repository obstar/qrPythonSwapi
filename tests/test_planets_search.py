from constants import TestData, StatusCode



def test_planets_get_search_is_successful(call):
    """
    1. Query planets to get Tatooine data
    2. Validate response data
    3. Loop through films
    4. For each film endpoint assert that status code is 200 OK 
    5. Assert that searched planet is on the planets list of the validated film
    """
    response_tatooine = call.planets.get(params=f"?search={TestData.TATOOINE}")
    assert response_tatooine.status_code == StatusCode.OK_200
    assert response_tatooine.data.count == 1
    assert response_tatooine.data.results[0].name == TestData.TATOOINE

    for film in response_tatooine.data.results[0].films:
        response_film = call.get_by_endpoint(film)
        assert response_film.status_code == StatusCode.OK_200
        assert response_tatooine.data.results[0].url in response_film.data.planets


def test_planets_get_search_uri_is_too_large(call):
    response = call.planets.get(params=f"?search={TestData.TOO_LARGE}", is_json=False)
    assert response.status_code == StatusCode.REQUEST_URI_TOO_LARGE_414
