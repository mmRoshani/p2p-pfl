def get_nested_value(d, key):
    keys = key.split(".")
    for k in keys:
        if isinstance(d, dict):
            d = d.get(k, None)
        else:
            return None
        if d is None:
            return None
    return d
