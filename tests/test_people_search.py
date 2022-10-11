from constants import InputData, StatusCode



def test_people_get_search_is_successful(call):
    """
        1. Query people to get luke skywalker data
        2. Validate response data
        3. Loop through films
        4. For each film endpoint assert that status code is 200 OK 
        5. Assert that searched character is on the character list of the validated film
    """
    response_luke = call.people.get(params=f"?search={InputData.LUKE_SKYWALKER}")
    assert response_luke.status_code == StatusCode.OK_200
    assert response_luke.data.count == 1
    assert response_luke.data.results[0].name == InputData.LUKE_SKYWALKER

    for film in response_luke.data.results[0].films:
        response_film = call.get_by_endpoint(film)
        assert response_film.status_code == StatusCode.OK_200
        assert response_luke.data.results[0].url in response_film.data.characters


def test_people_get_uri_is_too_large(call):
    response = call.people.get(params=f"?search={InputData.TOO_LARGE}", is_json=False)
    assert response.status_code == StatusCode.REQUEST_URI_TOO_LARGE_414
