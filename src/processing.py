from datetime import datetime


def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """
    Возвращает список словарей, у которых значение ключа 'state'
    совпадает с переданным значением.
    """
    if not isinstance(data, list):
        raise ValueError("Введены неверные данные")

    result = []

    for item in data:
        if isinstance(item, dict):
            if item.get("state") == state:
                result.append(item)

    return result


def sort_by_date(data: list, reverse: bool = True) -> list:
    """
    Сортирует данные по дате.
    Если формат даты не соответствует ISO или ключ отсутствует,
    возвращает 'Введены не верные данные.'
    """
    if not isinstance(data, list):
        raise ValueError("Введены не верные данные")

    try:
        # Пробуем отсортировать список
        return sorted(data, key=lambda item: datetime.fromisoformat(item["date"]), reverse=reverse)
    except KeyError, ValueError, TypeError:
        # KeyError — если нет ключа 'date'
        # ValueError — если формат строки не ISO (например, '30.06.2018' или '')
        # TypeError — если вместо словаря пришло что-то другое или дата не строка
        raise ValueError("Введены не верные данные")
