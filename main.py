from configs.logger.logger_bootstrap import logger_bootstrap
from decorators.get_execution_time import get_execution_time


@get_execution_time
def start() -> None:
    # config logger
    log = logger_bootstrap(
        instance_name=__name__,
        log_config_file_name="configs/logger/logging_config.yaml",
    )

    log.info("starting engine")
    pass


if __name__ == "__main__":
    start()
