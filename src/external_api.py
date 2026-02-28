import requests


def get_conversion(operation: dict) -> dict:
    """
    Конвертирует сумму операций из "USD" или "EUR" в "RUB"
    """
    actual_code = operation.get("operationAmount", {}).get("currency", {}).get("code")
    amount = operation.get("operationAmount", {}).get("amount")

    headers = {
        "apikey": "5ce3aJK7ZYMrBt24OtniuilwmiATTgot"
    }

    response = requests.get(f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={actual_code}&amount={amount}", headers=headers)

    data = response.json()
    converted_amount = data.get("result")

    operation["operationAmount"]["amount"] = converted_amount

    return operation


