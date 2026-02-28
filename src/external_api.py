import os

import requests
from dotenv import load_dotenv

load_dotenv()


def get_conversion(operation: dict) -> dict:
    """
    Конвертирует сумму операций из "USD" или "EUR" в "RUB"
    """
    actual_code = operation.get("operationAmount", {}).get("currency", {}).get("code")
    amount = operation.get("operationAmount", {}).get("amount")

    apilayer_token = os.getenv("APILAYER_TOKEN")
    headers = {"apikey": apilayer_token}
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={actual_code}&amount={amount}"
    response = requests.get(url, headers=headers)

    data = response.json()
    converted_amount = data.get("result")

    operation["operationAmount"]["amount"] = converted_amount

    return operation
