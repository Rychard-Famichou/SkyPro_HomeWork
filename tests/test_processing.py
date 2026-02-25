import pytest

from src import processing


# '''
# Тест сортировки стандарт + одинаковая дата
# '''
def test_filter_by_state(dict_list_processing):
    assert processing.filter_by_state(dict_list_processing) == [
        {"date": "2019-07-03T18:35:29.512364", "id": 414288290, "state": "EXECUTED"},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719571, "state": "EXECUTED"},
    ]


def test_sort_by_date(dict_list_processing):
    assert processing.sort_by_date(dict_list_processing) == [
        {"date": "2019-07-03T18:35:29.512364", "id": 414288290, "state": "EXECUTED"},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719571, "state": "EXECUTED"},
    ]


# '''
# Тест без ключа 'state'
# '''
def test_no_key_filter(dict_list_no_key):
    with pytest.raises(ValueError, match="Введены не верные данные"):
        processing.filter_by_state(dict_list_no_key)


def test_no_key_sort(dict_list_no_key):
    assert processing.sort_by_date(dict_list_no_key) == [
        {"date": "2019-07-03T18:35:29.512364", "id": 414288290},
        {"date": "2018-10-14T08:21:33.419441", "id": 615064591},
        {"date": "2018-09-12T21:27:25.241689", "id": 594226727},
        {"date": "2018-06-30T02:08:58.425572", "id": 939719570},
    ]


# '''
# Тест без ключа 'date'
# '''
def test_no_date_filter(dict_list_no_date):
    assert processing.filter_by_state(dict_list_no_date) == [
        {"id": 414288290, "state": "EXECUTED"},
        {"id": 939719570, "state": "EXECUTED"},
    ]


def test_no_date_sort(dict_list_no_date):
    with pytest.raises(ValueError, match="Введены не верные данные"):
        processing.sort_by_date(dict_list_no_date)


# '''
# Тест сортировки для статуса 'state'
# '''
def test_state(dict_list_state):
    assert processing.filter_by_state(dict_list_state) == []


# '''
# Тест сортировки для статуса 'date'
# '''
def test_date(dict_list_date):
    with pytest.raises(ValueError, match="Введены не верные данные"):
        processing.sort_by_date(dict_list_date)
