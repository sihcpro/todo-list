import logging


def setup_logger(config, log_name, log_level):
    logging.basicConfig(
        level="DEBUG", format=config.LOG_FORMAT, datefmt=config.LOG_DATEFMT,
    )

    logger = logging.getLogger(name=log_name)
    # handler = logging.StreamHandler()

    # handler.setLevel(log_level)
    # handler.emit = lambda x: x

    logger.setLevel(log_level)
    # logger.addHandler(handler)
    return logger
