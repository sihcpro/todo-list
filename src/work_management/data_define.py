from datetime import datetime
from pyrsistent import PClass, field

from base.entity import WorkStatus
from helper.factory import str_to_datetime
from helper.variant import nullabel


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
