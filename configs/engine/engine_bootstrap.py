import yaml
from configs.logger.logger_bootstrap import logger_bootstrap
from constants.keys import Keys
from constants.paths import Paths
from decorators.get_absolute_path import get_absolute_path
from utils.color import Color
from utils.get_nested_value import get_nested_value


@get_absolute_path
def engine_bootstrap(engine_config_file_name: str) -> dict:
    with open(engine_config_file_name, "rt") as f:
        config = yaml.safe_load(f.read())


    log = logger_bootstrap(
        instance_name=__name__,
        log_config_file_name=Paths.LOGGER_CONFIG,
    )

    log.info(Color.colored_bold("RM>> ", "red") + Color.colored(config, 'cyan'))

    for key in dir(Keys):
        if (
            not callable(getattr(Keys, key))
            and not key.startswith("__")
            and key.startswith("ENGINE_") # just asserting attributes that starts with `ENGINE_` key. 
        ):
            log.info(f"{Color.colored("asserting", "cyan")} configs for {Color.colored_underlined(getattr(Keys, key), 'cyan')} key [{Color.colored_bold("required", "light_red")}]" )
            value = get_nested_value(config, getattr(Keys, key))
            assert value is not None

    return config
