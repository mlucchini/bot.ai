import json


def to_json(obj):
    return json.dumps(obj, default=lambda o: __dump(o), indent=2, skipkeys=True)


def __dump(obj):
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    else:
        return None
