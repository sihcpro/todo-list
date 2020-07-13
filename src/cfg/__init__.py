from .load_config import Config
from .logger import setup_logger

config = Config("TodoList")
logger = setup_logger(config, config.APP_SORT_NAME, config.LOG_LEVEL)

__all__ = ("config", "logger")
