import os
from datetime import datetime

import pytest
from cfg import config, logger

testId = datetime.now().strftime("%Y%m%d-%H:%M:%S")
BASE_URL = "http://localhost:8088"
DEBUG = True


def getResponseData(response):
    return response.json()


@pytest.fixture
def constructUrl():
    def join(*args):
        return os.path.join(BASE_URL, *args)

    return join


@pytest.fixture
def testId():
    return testId


@pytest.fixture
def getItemId():
    def _getResp(response):
        data = getResponseData(response)
        logger.warning("data %r", data)
        return data["id"]

    return _getResp


@pytest.fixture
def logResponse():
    def _logResponse(response):
        if DEBUG:
            logger.info("response:", response.__dict__)

    return _logResponse


@pytest.fixture
def dateToStr():
    def _dateToStr(time):
        return time.strftime(config.DATE_FMT)

    return _dateToStr


@pytest.fixture
def compare():
    def _compare(response, data):
        response_data = getResponseData(response)
        return all(data[key] == response_data[key] for key in data)

    return _compare
