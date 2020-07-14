# Application
APP_SORT_NAME = "TODO"
APP_NAME = "Todo List"
APP_HOST = "0.0.0.0"
APP_PORT = 8088

# DataBase
SCHEMA_NAME = "TODO-LIST"
DB_CONNECTION = "postgres://postgres:postgres@localhost/local"

# Logger
LOG_LEVEL = "DEBUG"
LOG_FORMAT = (
    "%(asctime)s [ %(name)-10s - %(module)15s ] %(levelname)-7s: %(message)s"
)
LOG_DATEFMT = "%Y-%m-%d %H:%M:%S"

# Format
DATETIME_FMT = "%Y-%m-%d %H:%M:%S.%f"
DATE_FMT = "%Y-%m-%d"

# Validation
IGNORE_EXTRA_FIELDS = True

# Invironment
DEBUG = True
DEBUG_SQL = False
