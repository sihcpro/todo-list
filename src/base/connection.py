from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from cfg import config


def initEngine(echo=config.DEBUG_SQL):
    return create_engine(config.DB_CONNECTION, echo=echo)


def initSessionClass(bind=initEngine()):
    return sessionmaker(bind=bind)


def initSession():
    Session = initSessionClass()
    return Session()
