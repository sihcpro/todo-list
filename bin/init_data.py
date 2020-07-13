from base.connection import init_engine
from base.resource import Base
from work_management import resource as work_resource

Base.metadata.create_all(init_engine(echo=True))

__all__ = ("work_resource",)
