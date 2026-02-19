def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """
    Возвращает список словарей, у которых значение ключа 'state'
    совпадает с переданным значением.
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list, reverse: bool = True) -> list:
    """
    Возвращает новый список словарей,
    отсортированный по ключу 'date'.

    reverse=True — по убыванию (по умолчанию)
    reverse=False — по возрастанию
    """
    return sorted(data, key=lambda item: item.get("date"), reverse=reverse)
