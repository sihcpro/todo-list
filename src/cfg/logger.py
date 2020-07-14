import logging


def setupLogger(config, log_name, log_level):
    logging.basicConfig(
        level="DEBUG", format=config.LOG_FORMAT, datefmt=config.LOG_DATEFMT,
    )

    logger = logging.getLogger(name=log_name)

    logger.setLevel(log_level)
    return logger
