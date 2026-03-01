import logging


actual_logger = logging.getLogger("masks")
actual_logger.setLevel(logging.DEBUG)
actual_handler = logging.FileHandler("logs/masks.log", encoding="utf-8", mode="w")
actual_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
actual_handler.setFormatter(actual_formatter)
actual_logger.addHandler(actual_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате: XXXX XX** **** XXXX.
    """
    actual_logger.info("Старт работы функии: маскировка карты.")

    try:
        # Проверяем длину: если не 16, вызываем ошибку вручную
        if len(card_number) != 16:
            raise ValueError

        # Пробуем форматировать строку
        mask_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"

        actual_logger.info("Функция отработала в штатном режиме")
        return mask_card_number

    except (TypeError, ValueError, AttributeError) as e:
        # TypeError — если передали не строку
        # ValueError — если длина не 16
        # AttributeError — если у объекта нет метода среза
        actual_logger.error(f'Произошла ошибка: {e}', exc_info=True)
        return "Введены не верные данные."

    finally:
        actual_logger.info("Конец работы функии: маскировка карты.\n" + "=" * 30)


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счёта, оставляя только последние 4 цифры с префиксом **.
    """
    actual_logger.info("Старт работы функии: маскировка счета.")

    try:
        # Проверяем длину: если не 20, вызываем ошибку вручную
        if len(account_number) != 20:
            raise ValueError("Неверная длина номера счета")

        # Формируем маску: берем срез последних 4 символов
        actual_logger.info("Функция отработала в штатном режиме")
        return f"**{account_number[-4:]}"

    except (TypeError, ValueError, AttributeError) as e:
        # TypeError — если передано не строковое значение
        # ValueError — если длина не соответствует 20
        actual_logger.error(f'Произошла ошибка: {e}', exc_info=True)
        return "Введены не верные данные."

    finally:
        actual_logger.info("Конец работы функии: маскировка счета.\n" + "=" * 30)
