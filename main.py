from typing import Any

from src import generators
from src import processing
from src import readers
from src import regex
from src.config import OPERATIONS_JSON_FILE
from src.config import TRANSACTIONS_CSV_FILE
from src.config import TRANSACTIONS_EXCEL_FILE

FILE_READERS = {
    1: ("JSON", readers.read_data_json, OPERATIONS_JSON_FILE),
    2: ("CSV", readers.read_data_csv, TRANSACTIONS_CSV_FILE),
    3: ("XLSX", readers.read_data_excel, TRANSACTIONS_EXCEL_FILE),
}
ALLOWED_STATES = ["EXECUTED", "CANCELED", "PENDING"]


def get_reader() -> list[Any]:
    """
    Загружает файл на основе выбора пользователя
    """
    print("Выберите необходимый пункт меню:")
    for number, (name, _, _) in FILE_READERS.items():
        print(f"{number}. Получить информацию о транзакциях из {name}-файла")

    try:
        choice = int(input("\nВведите номер: "))
    except ValueError:
        print("Ошибка: нужно ввести число.")
        return []

    command = FILE_READERS.get(choice)

    if not command:
        print("Неверный пункт меню.")
        return []

    file_type, reader_func, path = command

    print(f"Для обработки выбран {file_type}-файл.")

    return reader_func(path)


def get_state() -> str | None:
    """
    Получает статус фильтрации
    """
    print("Введите статус, по которому необходимо выполнить фильтрацию.")
    print("Доступные для фильтровки статусы: ", end="")
    print(", ".join(ALLOWED_STATES))

    state = input("\nВведите статус: ").upper()

    if state not in ALLOWED_STATES:
        print(f'Статус операции "{state}" недоступен.')
        return None

    return state


def apply_state_filter(operations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    while True:
        state = get_state()
        if state:
            return processing.filter_by_state(operations, state)


def ask_yes_no(question: str) -> bool:
    """Запрашивает ответ Да/Нет"""
    print(question)
    answer = input().strip().lower()
    return answer == "да"


def get_sort_order() -> bool:
    """
    True — по убыванию
    False — по возрастанию
    """
    print("Отсортировать по возрастанию или по убыванию?")
    print("1. По возрастанию")
    print("2. По убыванию")

    choice = input("Введите номер: ")

    return choice != "1"


def print_operations(operations: list[dict[str, Any]]) -> None:
    for operation in operations:
        date = operation.get("date", "")
        description = operation.get("description", "")

        operation_amount = operation.get("operationAmount", {})
        amount = operation_amount.get("amount", "")
        currency = operation_amount.get("currency", {}).get("name", "")

        account_from = operation.get("from", "")
        account_to = operation.get("to", "")

        print(f"\n{date} {description}")
        print(f"{account_from} -> {account_to}")
        print(f"Сумма: {amount} {currency}")


def main() -> None:
    """
    Имитация работы приложения
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями. ")

    operations = get_reader()
    if not operations:
        print("Файл не содержит операций.")
        return

    while True:
        state = get_state()
        if state:
            break

    operations = processing.filter_by_state(operations, state)

    if ask_yes_no("Отсортировать операции по дате? Да/Нет"):
        reverse = get_sort_order()
        operations = processing.sort_by_date(operations, reverse)

    if ask_yes_no("Выводить только рублевые транзакции? Да/Нет"):
        operations = list(generators.filter_by_currency(operations, "RUB"))

    if ask_yes_no("Отфильтровать список транзакций по слову в описании? Да/Нет"):
        keyword = input("Введите ключевое слово: ").strip()
        operations = regex.filter_operations_by_description(operations, keyword)

    print("Распечатываю итоговый список транзакций...")
    print(f"\nВсего банковских операций в выборке: {len(operations)}")

    if not operations:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print_operations(operations)


if __name__ == "__main__":
    main()
