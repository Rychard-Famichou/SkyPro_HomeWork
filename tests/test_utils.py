import json
from pathlib import Path
from unittest.mock import mock_open
from unittest.mock import patch

import pytest
from pytest_lazy_fixtures import lf

from src import utils


@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "amount": "100"}]')
@patch("json.load")
def test_load_operations_success(mock_json_load, mock_file):
    """Тест успешного чтения корректного JSON-списка"""
    # Настраиваем мок json.load, чтобы он вернул список
    mock_json_load.return_value = [{"id": 1, "amount": "100"}]

    result = utils.load_operations("fake_path.json")

    assert result == [{"id": 1, "amount": "100"}]
    mock_file.assert_called_once_with(Path("fake_path.json"), encoding="utf-8")


@patch("builtins.open", side_effect=FileNotFoundError)
def test_load_operations_file_not_found(mock_file):
    """Тест ситуации, когда файл отсутствует"""
    result = utils.load_operations("non_existent.json")
    assert result == []


@patch("builtins.open", new_callable=mock_open, read_data="invalid json")
def test_load_operations_json_decode_error(mock_file):
    """Тест ошибки декодирования JSON"""
    with patch("json.load", side_effect=json.JSONDecodeError("msg", "doc", 0)):
        result = utils.load_operations("bad.json")
        assert result == []


@patch("builtins.open", new_callable=mock_open, read_data='{"not_a": "list"}')
def test_load_operations_not_a_list(mock_file):
    """Тест случая, когда в JSON не список, а другой объект"""
    with patch("json.load", return_value={"not_a": "list"}):
        result = utils.load_operations("object.json")
        assert result == []


@pytest.mark.parametrize(
    "dict_list, expected",
    [
        (lf("generators_dict_873106923"), 43318.34),
        (lf("generators_dict_594226727"), 67314.70),
    ],
)
def test_get_operation_amount_1(dict_list, expected):
    """Тест: "amount"="RUB" преобразуется в float"""
    assert utils.get_operation_amount(dict_list) == expected


def test_get_operation_amount_2(is_right_data_2):
    """Тест: "amount"="RUB" преобразуется в float"""
    data, expected = is_right_data_2
    assert utils.get_operation_amount(data) == expected
