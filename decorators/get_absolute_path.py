import functools
from pathlib import Path


def get_absolute_path(func):
    @functools.wraps(func)
    def wrapper_get_absolute_path(*args, **kwargs):
        _suf = "file_name"
        for key, val in kwargs.items():
            if key.endswith(_suf):
                kwargs[key] = Path(val).absolute()
        return func(*args, **kwargs)

    return wrapper_get_absolute_path
