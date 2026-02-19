from datetime import datetime

from src import masks


def mask_account_card(original_number: str) -> str:
    """
    Маскирует номер карты или счёта.
    """
    alpha_number = ""
    digit_number = ""

    if not isinstance(original_number, str):
        return "Введены не верные данные."
    elif len(original_number) < 16:
        return "Введены не верные данные."

    for char in original_number:
        if char.isalpha() or char == " ":
            alpha_number += char
        elif char.isdigit():
            digit_number += char

    if len(digit_number) not in [16, 20]:
        return "Введены не верные данные."
    if alpha_number == "Счет ":
        digit_number = masks.get_mask_account(digit_number)
    else:
        digit_number = masks.get_mask_card_number(digit_number)

    return alpha_number + digit_number


def get_date(original_date: str) -> str:
    """
    Форматирует дату по образцу.
    """
    new_date = original_date[:10]

    if not isinstance(original_date, str):
        return "Введены не верные данные."

    try:
        # Пытаемся преобразовать строку в объект даты
        # %Y - год (4 цифры), %m - месяц, %d - день
        date_obj = datetime.strptime(new_date, "%Y-%m-%d")

        # Преобразуем объект даты обратно в строку нужного формата
        return date_obj.strftime("%d.%m.%Y")

    except ValueError:
        # Если формат не совпал или дата некорректна (например, 2024-13-45)
        return "Ошибка: Неверный формат даты. Ожидается ГГГГ-ММ-ДД..."
