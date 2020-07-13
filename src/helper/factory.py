from datetime import datetime

from cfg import config


def str_to_datetime(value, fmt=config.DATETIME_FMT) -> datetime:
    return datetime.strptime(value, fmt)


def str_to_date(value, fmt=config.DATE_FMT) -> datetime:
    return datetime.strptime(value, fmt)


def to_json_value(value):
    if value is None:
        return value
    return str(value)
