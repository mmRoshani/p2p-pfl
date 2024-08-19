import functools
from pathlib import Path

from constants.keys import Keys


def get_absolute_path(func):
    @functools.wraps(func)
    def wrapper_get_absolute_path(*args, **kwargs):
        for key, val in kwargs.items():
            if key.endswith(Keys.file_name_suffix):
                kwargs[key] = Path(val).absolute()
        return func(*args, **kwargs)

    return wrapper_get_absolute_path
