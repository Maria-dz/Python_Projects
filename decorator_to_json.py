import json
from functools import wraps

def to_json(func):      #декоратор, превращающий результат в формат JSON
    @wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args,**kwargs)
        return json.dumps(result)
    return wrapped