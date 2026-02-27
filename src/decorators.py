from functools import wraps
from pathlib import Path


# Определяем корень проекта
BASE_DIR = Path(__file__).resolve().parent.parent
LOGS_DIR = BASE_DIR / "logs"


def log(filename=None):
    """
    Декоратор, который логирует начало и конец выполнения функции, ее результаты или возникшие ошибки.
    Должен принимать необязательный аргумент 'filename', который определяет,
    куда будут записываться логи (в файл или в консоль)
    """
    def write_log(message):
        if filename:
            LOGS_DIR.mkdir(exist_ok=True)
            file_path = LOGS_DIR / filename

            with open(file_path, "a", encoding="utf-8") as f:
                f.write(message + "\n")
        else:
            print(message)

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                write_log(f"{func.__name__} ok")
                return result

            except Exception as e:
                write_log(
                    f"{func.__name__} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}"
                )
                raise

        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)


@log()
def divide(x, y):
    return x / y

divide(1, 0)
