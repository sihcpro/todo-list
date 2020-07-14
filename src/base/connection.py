from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from cfg import config


def init_engine(echo=config.DEBUG_SQL):
    return create_engine(config.DB_CONNECTION, echo=echo)


def init_session_class(bind=init_engine()):
    return sessionmaker(bind=bind)


def init_session():
    Session = init_session_class()
    return Session()
