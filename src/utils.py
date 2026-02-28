import json
from pathlib import Path
from typing import Any
from src.config import OPERATIONS_FILE
from src import generators
from src import external_api


def load_operations(file_path: str | Path) -> list[dict[str, Any]]:
    """
    Преобразует JSON-файл в json-объект для python
    """
    path = Path(file_path)

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            return []

        return data

    except FileNotFoundError, json.JSONDecodeError:
        return []


def get_operation_amount(operation: dict) -> float:
    """
    Преобразование суммы операции в тип данных float
    """
    if operation.get("operationAmount", {}).get("currency", {}).get("code") != "RUB":
        external_api.get_conversion(operation)
        return float(operation["operationAmount"]["amount"])
    return float(operation.get("operationAmount", {}).get("amount"))


def get_work_experience():
    '''
    Имитация работы приложения
    '''
    counter = int(input("Введите количество операций: "))
    operations = load_operations(OPERATIONS_FILE)
    gen = generators.generate_operation(operations)
    for operation in range(1, counter + 1):
        amount = get_operation_amount(next(gen))
        print(f"{amount} RUB")

get_work_experience()