import yaml
from decorators.get_absolute_path import get_absolute_path


@get_absolute_path
def engine_bootstrap(engine_config_file_name: str) -> dict:

    with open(engine_config_file_name, "rt") as f:
        config = yaml.safe_load(f.read())
    print(config)

    return config
