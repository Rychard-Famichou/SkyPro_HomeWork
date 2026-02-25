import pytest


# Правильные карты!!!
@pytest.fixture(
    params=[
        ("1596837868705199", "1596 83** **** 5199"),  # Maestro
        ("7158300734726758", "7158 30** **** 6758"),  # MasterCard
        ("6831982476737658", "6831 98** **** 7658"),  # Visa Classic
        ("8990922113665229", "8990 92** **** 5229"),  # Visa Platinum
        ("5999414228426353", "5999 41** **** 6353"),  # Visa Gold
    ]
)
def card_data(request):
    return request.param


# Правильные счета!!!
@pytest.fixture(
    params=[
        ("64686473678894779589", "**9589"),  # Первый счёт
        ("35383033474447895560", "**5560"),  # Второй счёт
        ("73654108430135874305", "**4305"),  # Третий счёт
    ]
)
def account_data(request):
    return request.param


# Правильные комбо: карта/счет + номер!!!
@pytest.fixture(
    params=[
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),  # Maestro
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),  # MasterCard
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),  # Visa Classic
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),  # Visa Platinum
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),  # Visa Gold
        ("Счет 64686473678894779589", "Счет **9589"),  # Первый счёт
        ("Счет 35383033474447895560", "Счет **5560"),  # Второй счёт
        ("Счет 73654108430135874305", "Счет **4305"),  # Третий счёт
    ]
)
def account_card_data(request):
    return request.param


# Пустые данные или не правильный тип данных___
@pytest.fixture(
    params=[
        ("", "Введены не верные данные."),  # Пустая строка
        (" ", "Введены не верные данные."),  # Пробел
        ([], "Введены не верные данные."),  # Пустой лист
        (124567812345678, "Введены не верные данные."),  # int
    ]
)
def is_right_data(request):
    return request.param


# Ошибка ввода карты___
@pytest.fixture(
    params=[
        ("159683786870519", "Введены не верные данные."),  # Maestro - 1 знак
        ("15968378687051999", "Введены не верные данные."),  # Maestro + 1 знак
    ]
)
def is_card_data(request):
    return request.param


# Ошибка ввода счета___
@pytest.fixture(
    params=[
        ("6468647367889477958", "Введены не верные данные."),  # Первый счёт - 1 знак
        ("646864736788947795899", "Введены не верные данные."),  # Первый счёт + 1 знак
    ]
)
def is_account_data(request):
    return request.param


# Ошибка комбо ввода___
@pytest.fixture(
    params=[
        ("Maestro 159683786870519", "Введены не верные данные."),  # Maestro - 1 знак
        ("Maestro 15968378687051999", "Введены не верные данные."),  # Maestro + 1 знак
        ("Счет 6468647367889477958", "Введены не верные данные."),  # Первый счёт - 1 знак
        ("Счет 646864736788947795899", "Введены не верные данные."),  # Первый счёт + 1 знак
    ]
)
def is_kombo_data(request):
    return request.param


# Правильный список словарей операций!!! ( 2 одинаковые даты )
@pytest.fixture
def dict_list_processing():
    return [
        {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719571, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Список словарей операций без ключа 'state'___
@pytest.fixture
def dict_list_no_key():
    return [
        {"id": 414288290, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
    ]


# Список словарей операций без ключа 'date'___
@pytest.fixture
def dict_list_no_date():
    return [
        {"id": 414288290, "state": "EXECUTED"},
        {"id": 939719570, "state": "EXECUTED"},
        {"id": 594226727, "state": "CANCELED"},
        {"id": 615064591, "state": "CANCELED"},
    ]


# Список словарей операций для различных возможных значений статуса 'state'.
@pytest.fixture
def dict_list_state():
    return [
        {"id": 414288290, "state": "Finished", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "executed", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "Returned", "date": "2018-10-14T08:21:33.419441"},
    ]


# Список словарей операций для различных возможных значений статуса 'state'.
@pytest.fixture
def dict_list_date():
    return [
        {"id": 414288290, "state": "EXECUTED", "date": " "},
        {"id": 939719570, "state": "EXECUTED", "date": ""},
        {"id": 939719570, "state": "EXECUTED", "date": "30.06.2018"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018.06.30T02:08:58.425572"},
        {"id": 939719570, "state": "EXECUTED", "date": "20180630T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-19-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "0000-00-00T08:21:33.419441"},
    ]


# Список словарей операций для generators.py
@pytest.fixture
def generators_dict_list():
    return [
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
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
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
