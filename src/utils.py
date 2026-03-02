import json
import logging
from pathlib import Path
from typing import Any

from src import external_api

actual_logger = logging.getLogger("utils")
actual_logger.setLevel(logging.DEBUG)
actual_handler = logging.FileHandler("logs/utils.log", encoding="utf-8", mode="w")
actual_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
actual_handler.setFormatter(actual_formatter)
actual_logger.addHandler(actual_handler)


def load_operations(file_path: str | Path) -> list[dict[str, Any]]:
    """
    Преобразует JSON-файл в json-объект для python
    """
    path = Path(file_path)
    actual_logger.info("Старт работы функии: загрузка json-файла.")
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise TypeError("Данные в JSON не являются списком")

        actual_logger.info("Функция отработала в штатном режиме")
        return data

    except (FileNotFoundError, json.JSONDecodeError, TypeError) as e:
        actual_logger.error(f"Ошибка при загрузке: {e}")
        return []

    finally:
        actual_logger.info("Конец работы функии: загрузка json-файла.\n" + "=" * 30)


def get_operation_amount(operation: dict) -> float:
    """
    Преобразование суммы операции в тип данных float с обработкой валюты.
    """
    actual_logger.info("Старт работы функции: получение суммы операции(float) в RUB.")

    try:
        # Извлекаем данные (может возникнуть KeyError, если ключей нет)
        amount_data = operation["operationAmount"]
        currency_code = amount_data["currency"]["code"]
        raw_amount = amount_data["amount"]

        if currency_code != "RUB":
            # Предполагаем, что API обновляет данные внутри словаря или возвращает их
            external_api.get_conversion(operation)

            # Берем обновленное значение
            actual_logger.info("Конвертация валюты в RUB")
            return float(operation["operationAmount"]["amount"])

        actual_logger.info("Функция отработала в штатном режиме")
        return float(raw_amount)

    except (KeyError, TypeError, ValueError) as e:
        actual_logger.error(f"Ошибка при получении суммы: {e}. Данные: {operation}")
        # Возвращаем 0.0 или выбрасываем исключение дальше, в зависимости от логики
        return 0.0

    finally:
        actual_logger.info("Конец работы функции: получение суммы операции(float) в RUB.\n" + "=" * 30)
