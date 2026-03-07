import json
from pathlib import Path
from unittest.mock import MagicMock
from unittest.mock import mock_open
from unittest.mock import patch

import pandas as pd
import pytest

from src import readers


def test_read_data_json_success():
    expected = [{"id": 1, "val": "ok"}]

    with patch("builtins.open", mock_open(read_data=json.dumps(expected))):
        result = readers.read_data_json(Path("test.json"))

    assert result == expected


@pytest.mark.parametrize(
    "exception",
    [
        FileNotFoundError,
        json.JSONDecodeError("msg", "doc", 1),
        TypeError,
    ],
)
def test_read_data_json_errors(exception):

    with patch("builtins.open", side_effect=exception):
        result = readers.read_data_json(Path("fake.json"))

    assert result == []


@pytest.mark.parametrize(
    "reader_func, pd_method",
    [
        (readers.read_data_csv, "pandas.read_csv"),
        (readers.read_data_excel, "pandas.read_excel"),
    ],
)
def test_pandas_readers_success(reader_func, pd_method):

    with patch(pd_method) as mock_reader:

        mock_df = MagicMock()
        expected = [{"id": 1, "val": "ok"}]

        mock_df.to_dict.return_value = expected
        mock_reader.return_value = mock_df

        result = reader_func(Path("file"))

        assert result == expected
        mock_reader.assert_called_once()
        mock_df.to_dict.assert_called_once_with(orient="records")


@pytest.mark.parametrize(
    "reader_func, pd_method",
    [
        (readers.read_data_csv, "pandas.read_csv"),
        (readers.read_data_excel, "pandas.read_excel"),
    ],
)
@pytest.mark.parametrize(
    "exception",
    [
        FileNotFoundError,
        TypeError,
        ValueError,
        pd.errors.EmptyDataError(),
        pd.errors.ParserError("bad file"),
        UnicodeDecodeError("utf-8", b"", 0, 1, "bad"),
    ],
)
def test_pandas_readers_errors(reader_func, pd_method, exception):

    with patch(pd_method, side_effect=exception):

        result = reader_func(Path("file"))

        assert result == []
