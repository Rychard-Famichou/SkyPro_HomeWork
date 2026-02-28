import json
from pathlib import Path
from typing import Any


def load_operations(file_path: str | Path) -> list[dict[str, Any]]:
    path = Path(file_path)

    try:
        with open(path) as f:
            data = json.load(f)

        if not isinstance(data, list):
            return []

        return data

    except FileNotFoundError, json.JSONDecodeError:
        return []
