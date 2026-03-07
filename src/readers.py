import pandas as pd
import json
import logging
from pathlib import Path
from typing import Any


actual_logger = logging.getLogger("readers")
actual_logger.setLevel(logging.DEBUG)
actual_handler = logging.FileHandler("logs/readers.log", encoding="utf-8", mode="w")
actual_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
actual_handler.setFormatter(actual_formatter)
actual_logger.addHandler(actual_handler)


def load_operations(file_path: Path) -> list[dict[str, Any]]:
    """Возвращает список словарей из json"""
    actual_logger.info("Старт работы функии: загрузка json-файла.")
    try:
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise TypeError("Данные в JSON не являются списком")

        actual_logger.info("Функция отработала в штатном режиме")
        return data

    except (FileNotFoundError, json.JSONDecodeError, TypeError) as e:
        actual_logger.error(f"Ошибка при загрузке: {e}")
        return []

    finally:
        actual_logger.info("Конец работы функции: загрузка json-файла.\n" + "=" * 30)


def read_data_csv(csv_path: Path) -> list[dict[Any, Any]]:
    """Возвращает список словарей из csv"""
    actual_logger.info("Старт работы функии: загрузка csv-файла.")
    try:
        df: pd.DataFrame = pd.read_csv(csv_path)
        result: list[dict[Any, Any]] = df.to_dict(orient="records")
        actual_logger.info("Функция отработала в штатном режиме")
        return result

    except (FileNotFoundError, pd.errors.EmptyDataError) as e:
        # Файла нет или он пустой — возвращаем пустой список
        actual_logger.error(f"Ошибка при загрузке: {e}")
        return []
    except (pd.errors.ParserError, UnicodeDecodeError) as e:
        # Файл поврежден или кодировка не та
        actual_logger.error(f"Ошибка при загрузке: {e}")
        return []
    except Exception as e:
        # На всякий случай ловим остальные критические ошибки
        print(f"Произошла непредвиденная ошибка: {e}")
        actual_logger.error(f"Ошибка при загрузке: {e}")
        return []
    finally:
        actual_logger.info("Конец работы функции: загрузка json-файла.\n" + "=" * 30)


def read_data_excel(excel_path: Path) -> list[dict[Any, Any]]:
    """Возвращает список словарей из excel"""
    actual_logger.info("Старт работы функии: загрузка excel-файла.")
    try:
        df: pd.DataFrame = pd.read_excel(excel_path)
        result: list[dict[Any, Any]] = df.to_dict(orient="records")
        actual_logger.info("Функция отработала в штатном режиме")
        return result

    except (FileNotFoundError, TypeError, ValueError) as e:
        actual_logger.error(f"Ошибка при загрузке: {e}")
        return []
    except Exception as e:
        # На всякий случай ловим остальные критические ошибки
        print(f"Произошла непредвиденная ошибка: {e}")
        actual_logger.error(f"Ошибка при загрузке: {e}")
        return []
    finally:
        actual_logger.info("Конец работы функции: загрузка json-файла.\n" + "=" * 30)
