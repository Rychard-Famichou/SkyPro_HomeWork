from unittest.mock import patch
import requests
from src import external_api
import pytest



@patch('requests.get')
def test_external_api(mock_get):
    mock_get.return_value.json.return_value = {"result": 100.0}

    input_data = {
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"}
        }
    }

    expected_data = {
        "operationAmount": {
            "amount": 100.0,
            "currency": {"name": "USD", "code": "USD"}
        }
    }

    result = external_api.get_conversion(input_data)
    assert result == expected_data
