from base.connection import initEngine
from base.resource import Base
from work_management import resource as work_resource

Base.metadata.create_all(initEngine(echo=True))

__all__ = ("work_resource",)
