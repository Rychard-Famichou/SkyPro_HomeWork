from src import generators
from src import readers
from src import utils
from src import widget
from src.config import OPERATIONS_JSON_FILE
from src.config import TRANSACTIONS_CSV_FILE
from src.config import TRANSACTIONS_EXCEL_FILE


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


def main() -> None:
    """
    Имитация работы приложения
    """
    print("Здравствуйте.")

    counter = int(input("Введите количество операций: "))

    print()

    operations = utils.load_operations(OPERATIONS_JSON_FILE)
    gen = generators.generate_operation(operations)

    for operation in range(1, counter + 1):
        actual_operation = next(gen)
        date = get_operation_date(actual_operation)
        amount = utils.get_operation_amount(actual_operation)
        account_card_from = get_account_card_from(actual_operation)
        account_card_to = get_account_card_to(actual_operation)

        print(f"{date} : {amount} RUB")
        print(f"{account_card_from} : {account_card_to}")
        print()


def run_readers() -> None:
    """Проверка работы с data"""

    list_1 = readers.read_data_csv(TRANSACTIONS_CSV_FILE)
    list_2 = readers.read_data_excel(TRANSACTIONS_EXCEL_FILE)

    print(f"CSV data: {list_1}")
    print()
    print(f"Excel data: {list_2}")


if __name__ == "__main__":
    # main()
    run_readers()
