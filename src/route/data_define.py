from datetime import datetime

from base.entity import WorkStatus
from helper.factory import str_to_date, str_to_datetime
from helper.variant import nullabel
from pyrsistent import PClass, field


class AddWorkData(PClass):
    name = field(str, mandatory=True)
    starting_date = field(nullabel(datetime), factory=str_to_datetime)
    ending_date = field(nullabel(datetime), factory=str_to_datetime)
    status = field(WorkStatus, factory=WorkStatus)


class UpdateWorkData(PClass):
    name = field(str)
    starting_date = field(nullabel(datetime), factory=str_to_datetime)
    ending_date = field(nullabel(datetime), factory=str_to_datetime)
    status = field(WorkStatus, factory=WorkStatus)


class ShowWorkData(PClass):
    from_date = field(datetime, factory=str_to_date, mandatory=True)
    to_date = field(datetime, factory=str_to_date, mandatory=True)
