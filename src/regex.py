import re
from collections import Counter

from typing import Any


def filter_operations_by_description(
    operations: list[dict[str, Any]], search_string: str
) -> list[dict[str, Any]]:
    """
    Возвращает список операций, в описании которых есть строка поиска.
    """
    pattern = re.compile(search_string, re.IGNORECASE)

    return [
        operation
        for operation in operations
        if pattern.search(operation.get("description", ""))
    ]


def count_operations_by_category(
    operations: list[dict[str, Any]],
    categories: list[str]
) -> dict[str, int]:
    """
    Возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    """
    descriptions = [op.get("description", "") for op in operations]
    counter = Counter(descriptions)

    return {category: counter.get(category, 0) for category in categories}
