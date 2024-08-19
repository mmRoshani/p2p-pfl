import logging.config
import yaml
from decorators.get_absolute_path import get_absolute_path


@get_absolute_path
def logger_bootstrap(instance_name: str, log_config_file_name: str) -> logging.Logger:

    with open(log_config_file_name, "rt") as f:
        config = yaml.safe_load(f.read())

    logging.config.dictConfig(config)

    logger = logging.getLogger(instance_name)

    return logger
