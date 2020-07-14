import sqlalchemy

from base.connection import initEngine
from base.resource import Base
from cfg import config
from route import resource


engine = initEngine(echo=True)

if not engine.dialect.has_schema(engine, config.SCHEMA_NAME):
    engine.execute(sqlalchemy.schema.CreateSchema(config.SCHEMA_NAME))
Base.metadata.create_all(engine)

__all__ = ("resource",)
