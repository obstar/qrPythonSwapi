import logging
import pytest
from api.call import Call
from constants import Endpoint

logger = logging.getLogger("api")


@pytest.fixture(scope="session")
def call():
    logger.info(f"Start api tests, url is {Endpoint.SWAPI_DEV_API}")
    return Call()
