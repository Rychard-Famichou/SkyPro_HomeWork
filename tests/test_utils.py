import pytest
from pytest_lazy_fixtures import lf

from src import utils


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
