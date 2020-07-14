from sqlalchemy import Column, DateTime, Enum, Integer, Sequence, String

from base.entity import WorkStatus
from base.resource import Base
from cfg import config
from helper.factory import toJsonValue


class WorkResource(Base):
    __table_args__ = dict(schema=config.SCHEMA_NAME)
    __tablename__ = "work"

    id = Column(
        Integer,
        Sequence(
            name="work_id",
            start=0,
            increment=1,
            minvalue=0,
            nomaxvalue=True,
            schema=config.SCHEMA_NAME,
        ),
        primary_key=True,
    )

    name = Column(String(255))
    starting_date = Column(DateTime(timezone=False))
    ending_date = Column(DateTime(timezone=False))
    status = Column(Enum(WorkStatus))

    def asDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "starting_date": toJsonValue(self.starting_date),
            "ending_date": toJsonValue(self.ending_date),
            "status": toJsonValue(self.status),
        }
