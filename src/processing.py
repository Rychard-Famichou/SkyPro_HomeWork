from datetime import datetime


def filter_by_state(data: list, state: str = "EXECUTED"):
    """
    Возвращает список словарей, у которых значение ключа 'state'
    совпадает с переданным значением. Если ключ отсутствует — возвращает ошибку.
    """
    # Проверка: если входные данные не являются списком
    if not isinstance(data, list):
        return 'Введены не верные данные.'

    result = []

    for item in data:
        # Проверяем, является ли элемент словарем и есть ли в нем ключ 'state'
        if isinstance(item, dict) and "state" in item:
            if item.get("state") == state:
                result.append(item)
        else:
            # Если ключа нет или это не словарь
            return 'Введены не верные данные.'

    return result


def sort_by_date(data: list, reverse: bool = True):
    """
    Сортирует данные по дате.
    Если формат даты не соответствует ISO или ключ отсутствует,
    возвращает 'Введены не верные данные.'
    """
    if not isinstance(data, list):
        return "Введены не верные данные."

    try:
        # Пробуем отсортировать список
        return sorted(
            data,
            key=lambda item: datetime.fromisoformat(item["date"]),
            reverse=reverse
        )
    except (KeyError, ValueError, TypeError):
        # KeyError — если нет ключа 'date'
        # ValueError — если формат строки не ISO (например, '30.06.2018' или '')
        # TypeError — если вместо словаря пришло что-то другое или дата не строка
        return "Введены не верные данные."
