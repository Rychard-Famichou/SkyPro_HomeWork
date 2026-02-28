from functools import wraps
from pathlib import Path
from typing import Callable
from typing import Optional
from typing import ParamSpec
from typing import TypeVar

P = ParamSpec("P")
R = TypeVar("R")

BASE_DIR = Path(__file__).resolve().parent.parent
LOGS_DIR = BASE_DIR / "logs"


def log(filename: Optional[str] = None) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """
    Декоратор, который логирует начало и конец выполнения функции, ее результаты или возникшие ошибки.
    Должен принимать необязательный аргумент 'filename', который определяет,
    куда будут записываться логи (в файл или в консоль)
    """
    # def write_log(message: str, filename: Optional[str]) -> None:
    #     if filename:
    #         LOGS_DIR.mkdir(exist_ok=True)
    #         file_path = LOGS_DIR / filename
    #
    #         with open(file_path, "a", encoding="utf-8") as f:
    #             f.write(message + "\n")
    #     else:
    #         print(message)

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            try:
                result = func(*args, **kwargs)
                _write_log(f"{func.__name__} ok", filename)
                return result
            except Exception as e:
                _write_log(f"{func.__name__} error: {type(e).__name__}. " f"Inputs: {args}, {kwargs}", filename)
                raise

        return wrapper

    return decorator


def _write_log(message: str, filename: Optional[str]) -> None:
    if filename:
        LOGS_DIR.mkdir(exist_ok=True)
        file_path = LOGS_DIR / filename
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    else:
        print(message)


@log()
def add(x: int, y: int) -> int:
    """
    Функция сложения двух чисел.
    """
    return x + y


# if __name__ == "__main__":
#     add(1, 2)


@log()
def divide(x: int, y: int) -> float:
    """
    Функция деления двух чисел.
    """
    return x / y


# if __name__ == "__main__":
#     divide(1, 0)
