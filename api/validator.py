from requests import Response

class Validator:
    @staticmethod
    def structure(response: Response) -> Response:
        response.data = response.json()
        return response

    @staticmethod
    def return_endpoint_url(endpoint, params):
        if params is None:
            return f"{endpoint}"
        else:
            return f"{endpoint}{params}"
