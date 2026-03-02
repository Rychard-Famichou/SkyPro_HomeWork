from pathlib import Path
from unittest.mock import MagicMock
from unittest.mock import patch

import pandas as pd
import pytest

from src import readers


@pytest.mark.parametrize(
    "reader_func, pd_method, file_path",
    [
        (readers.read_data_csv, "pandas.read_csv", Path("test.csv")),
        (readers.read_data_excel, "pandas.read_excel", Path("test.xlsx")),
    ],
)
def test_readers_success(reader_func, pd_method, file_path):
    """Универсальный тест успешного чтения для CSV и Excel"""
    # Добавить json_load из utils?

    with patch(pd_method) as mock_pd:
        # Создаем фальшивый DataFrame
        mock_df = MagicMock()
        expected_data = [{"id": 1, "val": "ok"}]
        mock_df.to_dict.return_value = expected_data

        # Настраиваем мок pandas (read_csv/read_excel)
        mock_pd.return_value = mock_df

        # Выполняем
        result = reader_func(file_path)

        # Проверяем
        assert result == expected_data
        mock_pd.assert_called_once_with(file_path)
        mock_df.to_dict.assert_called_once_with(orient="records")


@pytest.mark.parametrize(
    "reader_func, pd_method",
    [(readers.read_data_csv, "pandas.read_csv"), (readers.read_data_excel, "pandas.read_excel")],
)
@pytest.mark.parametrize(
    "exception",
    [
        FileNotFoundError,
        pd.errors.EmptyDataError,
        pd.errors.ParserError,
        TypeError,
        ValueError,
        UnicodeDecodeError("utf-8", b"", 1, 2, "reason"),  # требует аргументы для инициализации
    ],
)
def test_all_readers_errors(pd_method, reader_func, exception):
    """Общий тест для CSV и Excel на обработку ошибок"""
    # Добавить json_load из utils?

    # Используем patch как контекстный менеджер, так как путь к методу меняется
    with patch(pd_method) as mock_method:
        mock_method.side_effect = exception

        result = reader_func(Path("fake_path"))

        assert result == []
        mock_method.assert_called_once()
