from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"

OPERATIONS_FILE = DATA_DIR / "operations.json"
