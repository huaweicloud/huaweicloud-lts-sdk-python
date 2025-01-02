import json
import time


def solv_log(x):
    n = 0
    while True:
        n += 1
        x >>= 7
        if x == 0:
            break
    return n


def _encode_obj(obj) -> dict:
    obj_dict = {}
    obj_dict.update(obj.__dict__)
    return obj_dict


def convert_obj2_json_str(obj):
    return json.dumps(obj, default=_encode_obj, indent=None, sort_keys=True)


def current_time_ms() -> int:
    return int((time.time() * 1000))


def current_time_ns() -> int:
    return time.time_ns()
