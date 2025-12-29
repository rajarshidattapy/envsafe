import json
from .exceptions import EnvError
from typing import Any


def parse_int(key, val) -> int:
    try:
        return int(val)
    except ValueError:
        raise EnvError(key, "expected int")


def parse_float(key, val) -> float:
    try:
        return float(val)
    except ValueError:
        raise EnvError(key, "expected float")


def parse_bool(key, val) -> bool:
    val = val.lower()
    if val in ("1", "true", "yes", "on"):
        return True
    if val in ("0", "false", "no", "off"):
        return False
    raise EnvError(key, "expected bool")


def parse_list(key, val, sep=",") -> list:
    return [v.strip() for v in val.split(sep) if v.strip()]


def parse_json(key, val) -> Any:
    try:
        return json.loads(val)
    except json.JSONDecodeError:
        raise EnvError(key, "expected valid JSON")
