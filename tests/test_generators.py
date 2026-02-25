from src import generators


# Тест правильных данных
def test_filter_by_currency(generators_dict_list):
    usd_expected = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]
    rub_expected = [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    assert list(generators.filter_by_currency(generators_dict_list, "USD")) == usd_expected
    assert list(generators.filter_by_currency(generators_dict_list, "RUB")) == rub_expected


# Тест правильных данных
def test_transaction_descriptions(generators_dict_list):
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]
    assert list(generators.transaction_descriptions(generators_dict_list)) == expected


# Тест правильных данных
def test_card_number_generator():
    expected = [
        "0000 0000 0000 9995",
        "0000 0000 0000 9996",
        "0000 0000 0000 9997",
        "0000 0000 0000 9998",
        "0000 0000 0000 9999",
    ]
    assert list(generators.card_number_generator(9995, 9999)) == expected


# Тест: Проверьте, что функция правильно обрабатывает случаи, когда транзакции в заданной валюте отсутствуют
def test_pl_filter(generators_dict_list):
    pl_transactions = generators.filter_by_currency(generators_dict_list, "PL")
    assert next(pl_transactions) == {"error": "Транзакции в заданной валюте отсутствуют"}


# Тест: Убедитесь, что генератор не завершается ошибкой при обработке пустого списка.
def test_empty_filter():
    empty_data = generators.filter_by_currency([], "USD")
    assert next(empty_data) == {"error": "Введены не верные данные."}


# Тест: Убедитесь, что генератор не завершается ошибкой при обработке пустого списка.
def test_empty_descriptions():
    empty_data = generators.transaction_descriptions([])
    assert next(empty_data) == "Введены не верные данные."
