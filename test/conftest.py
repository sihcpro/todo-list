import os
from datetime import datetime

import pytest
from cfg import config, logger

TEST_ID = datetime.now().strftime("%Y%m%d-%H:%M:%S")
BASE_URL = "http://localhost:8088"
DEBUG = True


def getResponseData(response):
    return response.json()


@pytest.fixture
def construct_url():
    def join(*args):
        return os.path.join(BASE_URL, *args)

    return join


@pytest.fixture
def test_id():
    return TEST_ID


@pytest.fixture
def get_item_id():
    def _get_resp(response):
        data = getResponseData(response)
        logger.warning("data %r", data)
        return data["id"]

    return _get_resp


@pytest.fixture
def log_response():
    def _log_response(response):
        if DEBUG:
            logger.info("response:", response.__dict__)

    return _log_response


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
