class Endpoint:
    SWAPI_DEV_API = "https://swapi.dev/api/"
    FILMS = f'{SWAPI_DEV_API}films/'
    PEOPLE = f'{SWAPI_DEV_API}people/'
    PLANETS = f'{SWAPI_DEV_API}planets/'
    SPECIES = f'{SWAPI_DEV_API}species/'
    STARSHIPS = f'{SWAPI_DEV_API}starships/'
    VEHICLES = f'{SWAPI_DEV_API}vehicles/'

class StatusCode:
    METHOD_NOT_ALLOWED_405 = 405
    OK_200 = 200