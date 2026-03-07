from src import generators
from src import processing
from src import readers
from src import regex
from src import utils
from src import widget
from src.config import OPERATIONS_JSON_FILE
from src.config import TRANSACTIONS_CSV_FILE
from src.config import TRANSACTIONS_EXCEL_FILE

FILE_READERS = {
    1: ("JSON", readers.read_data_json, OPERATIONS_JSON_FILE),
    2: ("CSV", readers.read_data_csv, TRANSACTIONS_CSV_FILE),
    3: ("XLSX", readers.read_data_excel, TRANSACTIONS_EXCEL_FILE),
}
ALLOWED_STATES = ["EXECUTED", "CANCELED", "PENDING"]


def get_operation_date(operation: dict) -> str:
    """Достаёт данные: дата операции"""
    # Если "date" нет, передаем пустую строку
    return widget.get_date(operation.get("date", ""))


def get_account_card_from(operation: dict) -> str:
    """Достаёт данные: номер, откуда совершена операция"""
    # Если "from" нет, передаем пустую строку
    return widget.mask_account_card(operation.get("from", ""))


def get_account_card_to(operation: dict) -> str:
    """Достаёт данные: номер, куда совершена операция"""
    # Если "to" нет, передаем пустую строку
    return widget.mask_account_card(operation.get("to", ""))


def get_reader() -> list:
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


def main() -> None:
    """
    Имитация работы приложения
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями. ")

    operations = get_reader()
    if not operations:
        return

    while True:
        state = get_state()
        if state is not None:
            break

    operations = processing.filter_by_state(operations, state)

    print("Отсортировать операции по дате? Да/Нет")
    date_ok = input().lower()

    print("Отсортировать по возрастанию или по убыванию? 1/2")
    sort_ok = input()
    if date_ok == "да":
        if sort_ok == "2":
            operations = processing.sort_by_date(operations)
        elif sort_ok == "1":
            operations = processing.sort_by_date(operations, False)

    print("Выводить только рублевые транзакции? Да/Нет")
    rub_ok = input().lower()
    if rub_ok == "да":
        operations = list(generators.filter_by_currency(operations, "RUB"))

    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    filter_ok = input().lower()
    if filter_ok == "да":
        word = input("Введите ключевое слово: ")
        operations = regex.filter_operations_by_description(operations, word)

    print("Распечатываю итоговый список транзакций...")
    print(f"\nВсего банковских операций в выборке: {len(operations)}")

    gen = generators.generate_operation(operations)

    for operation in range(1, len(operations) + 1):
        actual_operation = next(gen)
        date = get_operation_date(actual_operation)
        description = actual_operation.get("description", "")
        amount = utils.get_operation_amount(actual_operation)
        amount_name = actual_operation["operationAmount"]["currency"]["name"]
        account_card_from = get_account_card_from(actual_operation)
        account_card_to = get_account_card_to(actual_operation)

        print(f"\n{date} {description}")
        print(f"{account_card_from} -> {account_card_to}")
        print(f"Сумма: {amount} {amount_name}")

    if len(operations) < 1:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
