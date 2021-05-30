import logging

default_handler = logging.StreamHandler()  # type: ignore
default_handler.setFormatter(
    logging.Formatter("[%(asctime)s] %(levelname)s in [%(module)s, %(lineno)s]: %(message)s")
)

logging_config = {
    "critical": 50,
    "error": 40,
    "warning": 30,
    "info": 20,
    "debug": 10,
    "notset": 0
}


def get_logger(module, level="debug"):

    logger = logging.getLogger(module)

    if level not in logging_config.keys():
        raise Exception("Invalid logging level - {}. Supported values - {}".format(
            level, ','.join(logging_config.keys())))

    logger.setLevel(logging_config[level])
    logger.addHandler(default_handler)
    return logger
