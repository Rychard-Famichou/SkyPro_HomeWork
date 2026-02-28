import pytest
from pytest_lazy_fixtures import lf

from src import generators


# Тест простого генератора: вытаскивает словари из списка
def test_generate_operation(generators_dict_list):
    expected = generators_dict_list
    assert list(generators.generate_operation(generators_dict_list)) == expected


# Тест пустого списка
def test_generate_operation_empty():
    assert list(generators.generate_operation([])) == []


# Тест правильных данных
@pytest.mark.parametrize(
    "dict_list, code, expected_fixtures",
    [
        (
            lf("generators_dict_list"),
            "USD",
            [lf("generators_dict_939719570"), lf("generators_dict_142264268"), lf("generators_dict_895315941")]
        ),
        (
            lf("generators_dict_list"),
            "RUB",
            [lf("generators_dict_873106923"), lf("generators_dict_594226727")]
        ),
    ],
)
def test_filter_1(dict_list, code, expected_fixtures):
    result = list(generators.filter_by_currency(dict_list, code))
    assert result == expected_fixtures


# Тест правильных данных
@pytest.mark.parametrize(
    "dict_list, code, expected",
    [
        (lf("generators_dict_list"), "USD", lf("generators_dict_939719570")),
        (lf("generators_dict_list"), "RUB", lf("generators_dict_873106923")),
        ([], "USD", {"error": "Введены не верные данные."}),
        (lf("generators_dict_list"), "PL", {"error": "Транзакции в заданной валюте отсутствуют"}),
    ],
)
def test_filter_2(dict_list, code, expected):
    assert next(generators.filter_by_currency(dict_list, code)) == expected


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
@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            9999999999999998,
            9999999999999999,
            [
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
        (12345678, 12345678, ["0000 0000 1234 5678"]),
        (
            1,
            3,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
            ],
        ),
    ],
)
def test_card_number_generator(start, stop, expected):
    assert list(generators.card_number_generator(start, stop)) == expected


# Тест: Убедитесь, что генератор не завершается ошибкой при обработке пустого списка.
def test_empty_descriptions():
    empty_data = generators.transaction_descriptions([])
    assert next(empty_data) == "Введены не верные данные."
