from src import generators


# Тест правильных данных
def test_filter_by_currency(generators_dict_list):
    usd_transactions = generators.filter_by_currency(generators_dict_list, "USD")
    assert next(usd_transactions) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    assert next(usd_transactions) == {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    assert next(usd_transactions) == {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"}


# Тест правильных данных
def test_transaction_descriptions(generators_dict_list):
    descriptions = generators.transaction_descriptions(generators_dict_list)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"


# Тест правильных данных
def test_card_number_generator():
    card_number_generator = generators.card_number_generator(9995, 9999)
    assert next(card_number_generator) == "0000 0000 0000 9995"
    assert next(card_number_generator) == "0000 0000 0000 9996"
    assert next(card_number_generator) == "0000 0000 0000 9997"
    assert next(card_number_generator) == "0000 0000 0000 9998"
    assert next(card_number_generator) == "0000 0000 0000 9999"
