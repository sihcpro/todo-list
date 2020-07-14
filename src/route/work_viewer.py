import calendar
from datetime import timedelta

from sqlalchemy import Date, and_, cast, or_

from .data_define import ShowWorkData
from .resource import WorkResource


def config_work_viewer(Domain):
    session = Domain.session

    def getValidatedDate(param):
        date_data = ShowWorkData(
            from_date=param["from_date"][0], to_date=param["to_date"][0],
        )
        if date_data.from_date > date_data.to_date:
            raise ValueError("from_date must smaller than to_date")
        return date_data

    def getWorkInAPerius(from_date, to_date):
        record = {"from_date": str(from_date), "to_date": str(to_date)}
        if from_date == to_date:
            works = (
                session.query(WorkResource)
                .filter(
                    or_(
                        cast(WorkResource.starting_date, Date) == to_date,
                        cast(WorkResource.ending_date, Date) == to_date,
                        and_(
                            cast(WorkResource.starting_date, Date) < to_date,
                            cast(WorkResource.ending_date, Date) > to_date,
                        ),
                    )
                )
                .all()
            )
        else:
            works = (
                session.query(WorkResource)
                .filter(
                    or_(
                        and_(
                            WorkResource.starting_date >= from_date,
                            WorkResource.starting_date < to_date,
                        ),
                        and_(
                            WorkResource.ending_date >= from_date,
                            WorkResource.ending_date < to_date,
                        ),
                        and_(
                            WorkResource.starting_date <= from_date,
                            WorkResource.ending_date >= to_date,
                        ),
                    )
                )
                .all()
            )
        record["works"] = [work.as_dict() for work in works]
        return record

    @Domain.registerQuery("show-work-by-date")
    def showWorkByDate(data, identifier, param):
        date_data = getValidatedDate(param)
        date = date_data.from_date

        results = []
        while date <= date_data.to_date:
            results.append(getWorkInAPerius(date, date))
            date += timedelta(days=1)
        return results

    @Domain.registerQuery("show-work-by-week")
    def showWorkByWeek(data, identifier, param):
        date_data = getValidatedDate(param)
        date = date_data.from_date
        date = date - timedelta(days=date.weekday())

        results = []
        while date <= date_data.to_date:
            start_date = date
            end_date = date + timedelta(weeks=1) - timedelta(microseconds=1)
            results.append(getWorkInAPerius(start_date, end_date))
            date += timedelta(weeks=1)
        return results

    @Domain.registerQuery("show-work-by-month")
    def showWorkByMonth(data, identifier, param):
        date_data = getValidatedDate(param)
        date = date_data.from_date
        date = date - timedelta(days=date.day - 1)

        results = []
        while date <= date_data.to_date:
            days_in_month = calendar.monthrange(date.year, date.month)[1]
            start_date = date
            end_date = (
                date
                + timedelta(days=days_in_month)
                - timedelta(microseconds=1)
            )
            results.append(getWorkInAPerius(start_date, end_date))
            date += timedelta(days=days_in_month)
        return results
