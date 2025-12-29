import os
from dotenv import load_dotenv, find_dotenv

_loaded = False


def load_env_once() -> None:
    global _loaded
    if not _loaded:
        # Try find_dotenv first
        dotenv_path = find_dotenv()
        # If find_dotenv returns empty, fallback to current working directory
        if not dotenv_path or not os.path.isfile(dotenv_path):
            dotenv_path = os.path.join(os.getcwd(), ".env")
        # Only load if the file exists
        if os.path.isfile(dotenv_path):
            load_dotenv(dotenv_path, override=False)
        _loaded = True
