class Url:
    SWAPI_DEV_API = "https://swapi.dev/api/"

class Endpoint:
    FILMS = f'{Url.SWAPI_DEV_API}films/'
    PEOPLE = f'{Url.SWAPI_DEV_API}people/'
    PLANETS = f'{Url.SWAPI_DEV_API}planets/'
    SPECIES = f'{Url.SWAPI_DEV_API}species/'
    STARSHIPS = f'{Url.SWAPI_DEV_API}starships/'
    VEHICLES = f'{Url.SWAPI_DEV_API}vehicles/'

class StatusCode:
    METHOD_NOT_ALLOWED_405 = 405
    OK_200 = 200