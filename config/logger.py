import sys
import logging


def config_logger(
    instance_name: str = "__main__", log_level: int = logging.DEBUG
) -> logging.Logger:
    logger = logging.getLogger(instance_name)
    logger.setLevel(log_level)

    stdoutHandler = logging.StreamHandler(stream=sys.stdout)
    errHandler = logging.FileHandler("error.log")

    stdoutHandler.setLevel(log_level)
    errHandler.setLevel(logging.ERROR)

    fmt = logging.Formatter(
        "%(name)s: %(asctime)s | %(levelname)s | %(filename)s:%(lineno)s | %(process)d >>> %(message)s"
    )

    stdoutHandler.setFormatter(fmt)
    errHandler.setFormatter(fmt)

    logger.addHandler(stdoutHandler)
    logger.addHandler(errHandler)

    return logger

    """example"""
    # try:
    #     raise Exception("Failed to connect to database: 'my_db'")
    # except Exception as e:
    #     logger.error(e, exc_info=True)
