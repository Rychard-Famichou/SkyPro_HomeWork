import main
from main import FILE_READERS
from src import processing


def test_ask_yes_no_yes(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: "да")

    assert main.ask_yes_no("test") is True


def test_ask_yes_no_no(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: "нет")

    assert main.ask_yes_no("test") is False


def test_ask_yes_no_spaces(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda: "  Да ")

    assert main.ask_yes_no("test") is True


def test_get_sort_order_ascending(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")

    assert main.get_sort_order() is False


def test_get_sort_order_descending(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2")

    assert main.get_sort_order() is True


def test_get_state_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "executed")

    assert main.get_state() == "EXECUTED"


def test_get_state_invalid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "wrong")

    assert main.get_state() is None


def test_print_operations(capsys):
    operations = [
        {
            "date": "2023-01-01",
            "description": "Перевод",
            "operationAmount": {
                "amount": "100",
                "currency": {"name": "RUB"},
            },
            "from": "Card",
            "to": "Account",
        }
    ]

    main.print_operations(operations)

    captured = capsys.readouterr()

    assert "Перевод" in captured.out
    assert "100 RUB" in captured.out


def test_get_reader(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "1")

    def fake_reader(path):
        return [{"id": 1}]

    monkeypatch.setitem(
        FILE_READERS,
        1,
        ("JSON", fake_reader, "fake_path"),
    )

    result = main.get_reader()

    assert result == [{"id": 1}]


def test_apply_state_filter(monkeypatch):

    monkeypatch.setattr("builtins.input", lambda _: "executed")

    monkeypatch.setattr(
        processing,
        "filter_by_state",
        lambda ops, state: [{"filtered": True}],
    )

    result = main.apply_state_filter([{"id": 1}])

    assert result == [{"filtered": True}]


def test_main_runs(monkeypatch):

    monkeypatch.setattr("builtins.input", lambda *args: "нет")

    monkeypatch.setattr("main.get_reader", lambda: [])

    main.main()
