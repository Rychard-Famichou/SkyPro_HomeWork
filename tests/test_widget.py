import pytest

from src import widget


# '''
# Тест комбо-маскировки: 8 вариантов
# '''
def test_mask_account_card(account_card_data):
    account_card, expected = account_card_data
    assert widget.mask_account_card(account_card) == expected


# '''
# Тест форматирования даты: 5 вариантов
# '''
@pytest.mark.parametrize(
    "string_date, expected_result",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-13-11T02:26:18.671407", "Ошибка: Неверный формат даты. Ожидается ГГГГ-ММ-ДД..."),
        ("2024-03-41T02:26:18.671407", "Ошибка: Неверный формат даты. Ожидается ГГГГ-ММ-ДД..."),
        ("0000-00-00T02:26:18.671407", "Ошибка: Неверный формат даты. Ожидается ГГГГ-ММ-ДД..."),
        ("20240311T02:26:18.671407", "Ошибка: Неверный формат даты. Ожидается ГГГГ-ММ-ДД..."),
    ],
)
def test_get_date(string_date, expected_result):
    assert widget.get_date(string_date) == expected_result


# '''
# Тест данных: 4 варианта
# '''
def test_data_account_card(is_right_data):
    data, expected = is_right_data
    assert widget.mask_account_card(data) == expected


# '''
# Тест ввода длины: 2 варианта
# '''
def test_input_card_number(is_kombo_data):
    data, expected = is_kombo_data
    assert widget.mask_account_card(data) == expected
