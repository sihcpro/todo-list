from datetime import datetime, timedelta
from random import randrange, seed

import requests


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

    def testShowWorkByDate(self, construct_url, test_id, dateToStr):
        seed(test_id)
        params = {
            "from_date": dateToStr(
                datetime.utcnow() - timedelta(days=randrange(10))
            ),
            "to_date": dateToStr(
                datetime.utcnow() + timedelta(days=randrange(10))
            ),
        }

        response = self.session.get(
            url=construct_url("show-work-by-date"), params=params,
        )
        assert response.status_code in self.SUCCESS_CODE

    def testShowWorkByWeek(self, construct_url, test_id, dateToStr):
        seed(test_id)
        params = {
            "from_date": dateToStr(
                datetime.utcnow() - timedelta(days=randrange(20))
            ),
            "to_date": dateToStr(
                datetime.utcnow() + timedelta(days=randrange(20))
            ),
        }

        response = self.session.get(
            url=construct_url("show-work-by-week"), params=params,
        )
        assert response.status_code in self.SUCCESS_CODE

    def testShowWorkByMonth(self, construct_url, test_id, dateToStr):
        seed(test_id)
        params = {
            "from_date": dateToStr(
                datetime.utcnow() - timedelta(days=randrange(100))
            ),
            "to_date": dateToStr(
                datetime.utcnow() + timedelta(days=randrange(100))
            ),
        }

        response = self.session.get(
            url=construct_url("show-work-by-month"), params=params,
        )
        assert response.status_code in self.SUCCESS_CODE
