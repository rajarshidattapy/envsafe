import os
from .loaders import load_env_once
from .exceptions import EnvError
from . import parsers
from typing import Any


class Env:
    def load_dotenv(self) -> None:
        load_env_once()

    def _get(self, key, default) -> str:
        val = os.getenv(key)
        if val is None:
            if default is not None:
                return default
            raise EnvError(key, "missing")
        return val

    def get_str(self, key, default=None) -> str:
        return self._get(key, default)

    def get_int(self, key, default=None) -> int:
        val = self._get(key, default)
        return val if val is None else parsers.parse_int(key, val)

    def get_float(self, key, default=None) -> float:
        val = self._get(key, default)
        return val if val is None else parsers.parse_float(key, val)

    def get_bool(self, key, default=None) -> bool:
        val = self._get(key, default)
        return val if val is None else parsers.parse_bool(key, val)

    def get_list(self, key, default=None, *, sep=",") -> list:
        val = self._get(key, default)
        return val if val is None else parsers.parse_list(key, val, sep)

    def get_json(self, key, default=None) -> Any:
        val = self._get(key, default)
        return val if val is None else parsers.parse_json(key, val)

    def require(self, *keys):
        for key in keys:
            if os.getenv(key) is None:
                raise EnvError(key, "missing")
