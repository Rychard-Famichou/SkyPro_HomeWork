import pytest
from src import decorators
from src.decorators import log


def test_add(capsys):
    """
    Тест (__консоль__) с правильным вариантом.
    """
    decorators.add(1, 2)
    captured = capsys.readouterr()
    assert captured.out.strip() == \
           "add ok"


def test_add_error(capsys):
    """
    Тест (__консоль__) возбуждения ошибки: не верный тип данных.
    """
    with pytest.raises(TypeError):
        decorators.add(1, "2")

    captured = capsys.readouterr()
    assert captured.out.strip() == \
           "add error: TypeError. Inputs: (1, '2'), {}"


def test_divide(capsys):
    """
    Тест (__консоль__) с правильным вариантом.
    """
    decorators.divide(2, 1)
    captured = capsys.readouterr()
    assert captured.out.strip() == \
           "divide ok"


def test_divide_error(capsys):
    """
    Тест (__консоль__) возбуждения ошибки: на ноль делить нельзя.
    """
    with pytest.raises(ZeroDivisionError):
        decorators.divide(1, 0)

    captured = capsys.readouterr()
    assert captured.out.strip() == \
        "divide error: ZeroDivisionError. Inputs: (1, 0), {}"


def test_log_file_ok(tmp_path):
    """
    Тест (__файл__) с правильным вариантом.
    """
    log_file = tmp_path / "test_log.txt"

    @log(filename=log_file.name)
    def add(x, y):
        return x + y

    # временно подменим папку logs
    from src import decorators
    decorators.LOGS_DIR = tmp_path

    add(2, 3)

    content = log_file.read_text(encoding="utf-8").strip()
    assert content == "add ok"


def test_log_file_error(tmp_path):
    """
    Тест (__файл__) возбуждения ошибки: на ноль делить нельзя.
    """
    log_file = tmp_path / "test_log.txt"

    from src import decorators
    decorators.LOGS_DIR = tmp_path

    @log(filename=log_file.name)
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    content = log_file.read_text(encoding="utf-8").strip()
    assert content == \
        "divide error: ZeroDivisionError. Inputs: (1, 0), {}"
