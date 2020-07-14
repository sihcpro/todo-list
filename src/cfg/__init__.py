from .load_config import Config
from .logger import setupLogger

config = Config("TodoList")
logger = setupLogger(config, config.APP_SORT_NAME, config.LOG_LEVEL)

__all__ = ("config", "logger")
