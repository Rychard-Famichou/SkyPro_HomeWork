from collections.abc import Iterator


def filter_by_currency(transactions: list, currency_code: str) -> Iterator[dict]:
    """
    Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной.
    """
    if not transactions:
        yield {"error": "Введены не верные данные."}
        return

    found = False

    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            found = True
            yield transaction

    if not found:
        yield {"error": "Транзакции в заданной валюте отсутствуют"}


def transaction_descriptions(transactions: list) -> Iterator[str]:
    """
    Возвращает описание каждой операции по очереди.
    """
    if not transactions:
        yield "Введены не верные данные."
        return

    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в формате:
    XXXX XXXX XXXX XXXX
    """
    for number in range(start, stop + 1):
        # преобразуем число в строку из 16 цифр с ведущими нулями
        card_number = f"{number:016d}"

        # форматируем по 4 цифры
        formatted = f"{card_number[:4]} " f"{card_number[4:8]} " f"{card_number[8:12]} " f"{card_number[12:]}"

        yield formatted
