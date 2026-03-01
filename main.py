
from src import generators
from src import utils
from src import widget
from src.config import OPERATIONS_FILE


def get_operation_date(operation: dict) -> str:
    return widget.get_date(operation.get("date"))


def get_account_card_from(operation: dict) -> str:
    return widget.mask_account_card(operation.get("from"))


def get_account_card_to(operation: dict) -> str:
    return widget.mask_account_card(operation.get("to"))


def main() -> None:
    """
    Имитация работы приложения
    """
    print("Здравствуйте.")

    counter = int(input("Введите количество операций: "))

    print()

    operations = utils.load_operations(OPERATIONS_FILE)
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


if __name__ == "__main__":
    main()
