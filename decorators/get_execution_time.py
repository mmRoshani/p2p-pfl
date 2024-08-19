import functools
import time
from constants.paths import Paths
from configs.logger.logger_bootstrap import logger_bootstrap
from utils.color import Color


def get_execution_time(func):
    @functools.wraps(func)
    def wrapper_get_execution_time(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        run_time_pretty = f"{run_time:.4f}"
        
        log = logger_bootstrap(
            instance_name=__name__,
            log_config_file_name=Paths.logger_config,
        )

        log.info(f"finished {Color.colored_bold(func.__name__ + "()", 'green')} in {Color.colored_underlined(run_time_pretty, 'light_green')} secs")
        return value

    return wrapper_get_execution_time
