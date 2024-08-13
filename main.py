from config.logger import config_logger


def start() -> None:
    # config logger
    log = config_logger(instance_name=__name__)

    log.info("Starting engine")
    pass


if __name__ == "__main__":
    start()
