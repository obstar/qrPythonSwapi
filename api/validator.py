from requests import Response

class Validator:
    @staticmethod
    def structure(response: Response) -> Response:
        response.data = response.json()
        return response
