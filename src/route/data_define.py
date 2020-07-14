from datetime import datetime
from pyrsistent import PClass, field

from base.entity import WorkStatus
from helper.factory import strToDate, strToDatetime
from helper.variant import nullabel


class AddWorkData(PClass):
    name = field(str, mandatory=True)
    starting_date = field(nullabel(datetime), factory=strToDatetime)
    ending_date = field(nullabel(datetime), factory=strToDatetime)
    status = field(WorkStatus, factory=WorkStatus)


class UpdateWorkData(PClass):
    name = field(str)
    starting_date = field(nullabel(datetime), factory=strToDatetime)
    ending_date = field(nullabel(datetime), factory=strToDatetime)
    status = field(WorkStatus, factory=WorkStatus)


class ShowWorkData(PClass):
    from_date = field(datetime, factory=strToDate, mandatory=True)
    to_date = field(datetime, factory=strToDate, mandatory=True)
