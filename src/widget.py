from typing import Union

from src import masks


def mask_account_card(original_number: Union[str]) -> str:
    """
    Маскирует номер карты или счёта.
    """
    alpha_number = ""
    digit_number = ""

    for char in original_number:
        if char.isalpha() or char == " ":
            alpha_number += char
        elif char.isdigit():
            digit_number += char

    if alpha_number == "Счет ":
        digit_number = masks.get_mask_account(digit_number)
    else:
        digit_number = masks.get_mask_card_number(digit_number)

    return alpha_number + digit_number


def get_date(original_date: Union[str]) -> str:
    """
    Форматирует дату по образцу.
    """
    formatted_date = ""
    formatted_date += original_date[8:10] + "." + original_date[5:7] + "." + original_date[:4]
    return formatted_date
