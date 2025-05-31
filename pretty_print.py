def info(msg: str) -> None:
    print(f"\033[0;32mINFO: {msg}\033[0m")


def warning(msg: str) -> None:
    print(f"\033[0;33mWARNING: {msg}\033[0m")


def error(msg: str) -> None:
    print(f"\033[0;31mERROR: {msg}\033[0m")
