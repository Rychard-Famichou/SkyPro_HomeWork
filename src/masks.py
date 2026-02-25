def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты.
    """
    if not isinstance(card_number, str):
        return "Введены не верные данные."
    if len(card_number) == 16:
        mask_card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[12:]
        return mask_card_number
    return "Введены не верные данные."


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счёта.
    """
    if not isinstance(account_number, str):
        return "Введены не верные данные."
    if len(account_number) == 20:
        mask_account_number = "**" + account_number[-4:]
        return mask_account_number
    return "Введены не верные данные."
