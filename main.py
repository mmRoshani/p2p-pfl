from configs.logger.logger_bootstrap import logger_bootstrap
from configs.engine.engine_bootstrap import engine_bootstrap
from constants.keys import Keys
from constants.paths import Paths
from decorators.get_execution_time import get_execution_time
from utils.color import Color


@get_execution_time
def engine() -> None:
    # config logger
    log = logger_bootstrap(
        instance_name=__name__,
        log_config_file_name=Paths.LOGGER_CONFIG,
    )

    log.info(Color.colored("engine started", "yellow"))

    log.info(Color.colored("loading engine config", "magenta"))
    engine_config = engine_bootstrap(Paths.ENGINE_CONFIG)
    engine_release: str = str(engine_config.get(Keys.ENGINE_RELEASE))

    log.info(Color.colored(f"engine {Color.colored("(release: " + engine_release + ")", "green")} config loaded successfully", "green"))

    pass


if __name__ == "__main__":
    engine()
