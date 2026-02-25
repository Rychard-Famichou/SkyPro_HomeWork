def filter_by_currency(transactions: list, currency_code: str):
    """
    Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной.
    """
    for transaction in transactions:
        if (
            transaction.get("operationAmount", {})
            .get("currency", {})
            .get("code") == currency_code
        ):
            yield transaction


def transaction_descriptions(transactions: list):
    """
    Возвращает описание каждой операции по очереди.
    """
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int, end: int):
    """
    Генератор номеров банковских карт в формате:
    XXXX XXXX XXXX XXXX
    """
    for number in range(start, end + 1):
        # преобразуем число в строку из 16 цифр с ведущими нулями
        card_number = f"{number:016d}"

        # форматируем по 4 цифры
        formatted = (
            f"{card_number[:4]} "
            f"{card_number[4:8]} "
            f"{card_number[8:12]} "
            f"{card_number[12:]}"
        )

        yield formatted
