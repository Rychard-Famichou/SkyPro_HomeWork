from src import regex


def test_filter_operations_by_description_basic():

    operations = [
        {"description": "Перевод организации"},
        {"description": "Оплата услуг"},
        {"description": "Перевод с карты"},
    ]

    result = regex.filter_operations_by_description(operations, "Перевод")

    assert len(result) == 2


def test_filter_operations_case_insensitive():

    operations = [
        {"description": "Перевод организации"},
        {"description": "оплата услуг"},
    ]

    result = regex.filter_operations_by_description(operations, "перевод")

    assert result == [{"description": "Перевод организации"}]


def test_filter_operations_no_matches():

    operations = [
        {"description": "Оплата услуг"},
        {"description": "Покупка"},
    ]

    result = regex.filter_operations_by_description(operations, "Перевод")

    assert result == []


def test_count_operations_by_category_basic():

    operations = [
        {"description": "Перевод"},
        {"description": "Перевод"},
        {"description": "Оплата"},
    ]

    categories = ["Перевод", "Оплата"]

    result = regex.count_operations_by_category(operations, categories)

    assert result == {
        "Перевод": 2,
        "Оплата": 1,
    }


def test_count_operations_category_not_present():

    operations = [
        {"description": "Перевод"},
        {"description": "Перевод"},
    ]

    categories = ["Перевод", "Оплата"]

    result = regex.count_operations_by_category(operations, categories)

    assert result == {
        "Перевод": 2,
        "Оплата": 0,
    }


def test_count_operations_empty_list():

    result = regex.count_operations_by_category([], ["Перевод"])

    assert result == {"Перевод": 0}
