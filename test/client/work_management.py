from datetime import datetime, timedelta
from random import choice, randrange, seed

import requests

import pytest


class TestWorkItemAPI:
    result = {}
    SUCCESS_CODE = [200, 201, 202, 203, 204, 205, 206, 207, 208, 226]

    @property
    def session(self):
        if hasattr(self, "_session"):
            return self._session
        self._session = requests.Session()
        self._session.verify = False
        return self._session

    @pytest.mark.create_work
    def testAddWork(
        self, construct_url, test_id, get_item_id, log_response, compare
    ):
        seed(test_id)
        data = {
            "name": f"Work {test_id}",
            "starting_date": str(
                datetime.utcnow() - timedelta(days=randrange(3))
            ),
            "ending_date": str(
                datetime.utcnow() + timedelta(days=randrange(3))
            ),
            "status": choice(["Planning", "Doing", "Complete"]),
        }
        response = self.session.post(url=construct_url("add-work"), json=data,)
        log_response(response)
        assert response.status_code in self.SUCCESS_CODE
        self.result["work_id"] = get_item_id(response)

        response = self.session.get(
            url=construct_url("show-work", str(self.result["work_id"]))
        )
        assert response.status_code in self.SUCCESS_CODE
        assert compare(response, data) is True

    def testUpdateWork(self, construct_url, test_id, log_response, compare):
        seed(test_id)
        data = {
            "name": f"Work {test_id}",
            "starting_date": str(
                datetime.utcnow() - timedelta(days=randrange(3))
            ),
            "ending_date": str(
                datetime.utcnow() + timedelta(days=randrange(3))
            ),
            "status": choice(["Planning", "Doing", "Complete"]),
        }
        response = self.session.post(
            url=construct_url("update-work", str(self.result["work_id"])),
            json=data,
        )
        log_response(response)
        assert response.status_code in self.SUCCESS_CODE

        response = self.session.get(
            url=construct_url("show-work", str(self.result["work_id"]))
        )
        assert response.status_code in self.SUCCESS_CODE
        assert compare(response, data) is True

    def testDeleteWork(self, construct_url, log_response):
        response = self.session.post(
            url=construct_url("delete-work", str(self.result["work_id"])),
        )
        log_response(response)
        assert response.status_code in self.SUCCESS_CODE

        response = self.session.get(
            url=construct_url("show-work", str(self.result["work_id"]))
        )
        assert response.status_code not in self.SUCCESS_CODE
