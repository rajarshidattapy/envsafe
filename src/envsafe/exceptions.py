class EnvError(RuntimeError):
    def __init__(self, key: str, message: str) -> None:
        super().__init__(f"[envsafe] {key}: {message}")
