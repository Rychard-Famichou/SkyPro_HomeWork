from src import masks


'''
Тест маскировки: 5 разных карт
'''
def test_mask_card_number(card_data):
    number, expected = card_data
    assert masks.get_mask_card_number(number) == expected


'''
Тест маскировки: 3 разных счета
'''
def test_mask_account(account_data):
    number, expected = account_data
    assert masks.get_mask_account(number) == expected


'''
Тест данных: 4 варианта
'''
def test_data_card_number(is_right_data):
    data, expected = is_right_data
    assert masks.get_mask_card_number(data) == expected


def test_data_account(is_right_data):
    data, expected = is_right_data
    assert masks.get_mask_account(data) == expected


'''
Тест ввода длины: 2 варианта
'''
def test_input_card_number(is_card_data):
    data, expected = is_card_data
    assert masks.get_mask_card_number(data) == expected


def test_input_account(is_account_data):
    data, expected = is_account_data
    assert masks.get_mask_account(data) == expected
