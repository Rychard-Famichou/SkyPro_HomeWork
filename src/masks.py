from typing import Union


def get_mask_card_number(card_number: Union[str]) -> str:
    """
    Маскирует номер карты.
    """
    if len(card_number) == 16:
        mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
        return mask_card_number
    return "Не корректный номер."


def get_mask_account(account_number: Union[str]) -> str:
    """
    Маскирует номер счёта.
    """
    mask_account_number = "**" + account_number[-4:]
    return mask_account_number
