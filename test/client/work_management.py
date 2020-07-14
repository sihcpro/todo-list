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
        self, constructUrl, testId, getItemId, logResponse, compare
    ):
        seed(testId)
        data = {
            "name": f"Work {testId}",
            "starting_date": str(
                datetime.utcnow() - timedelta(days=randrange(3))
            ),
            "ending_date": str(
                datetime.utcnow() + timedelta(days=randrange(3))
            ),
            "status": choice(["Planning", "Doing", "Complete"]),
        }
        response = self.session.post(url=constructUrl("add-work"), json=data,)
        logResponse(response)
        assert response.status_code in self.SUCCESS_CODE
        self.result["work_id"] = getItemId(response)

        response = self.session.get(
            url=constructUrl("show-work", str(self.result["work_id"]))
        )
        assert response.status_code in self.SUCCESS_CODE
        assert compare(response, data) is True

    def testUpdateWork(self, constructUrl, testId, logResponse, compare):
        seed(testId)
        data = {
            "name": f"Work {testId}",
            "starting_date": str(
                datetime.utcnow() - timedelta(days=randrange(3))
            ),
            "ending_date": str(
                datetime.utcnow() + timedelta(days=randrange(3))
            ),
            "status": choice(["Planning", "Doing", "Complete"]),
        }
        response = self.session.post(
            url=constructUrl("update-work", str(self.result["work_id"])),
            json=data,
        )
        logResponse(response)
        assert response.status_code in self.SUCCESS_CODE

        response = self.session.get(
            url=constructUrl("show-work", str(self.result["work_id"]))
        )
        assert response.status_code in self.SUCCESS_CODE
        assert compare(response, data) is True

    def testDeleteWork(self, constructUrl, logResponse):
        response = self.session.post(
            url=constructUrl("delete-work", str(self.result["work_id"])),
        )
        logResponse(response)
        assert response.status_code in self.SUCCESS_CODE

        response = self.session.get(
            url=constructUrl("show-work", str(self.result["work_id"]))
        )
        assert response.status_code not in self.SUCCESS_CODE
