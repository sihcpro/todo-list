from datetime import datetime

from cfg import config
from enum import Enum


def strToDatetime(value, fmt=config.DATETIME_FMT) -> datetime:
    return datetime.strptime(value, fmt)


def strToDate(value, fmt=config.DATE_FMT) -> datetime:
    return datetime.strptime(value, fmt)


def toJsonValue(value):
    if value is None:
        return value
    if isinstance(value, Enum):
        return value.name
    return str(value)
