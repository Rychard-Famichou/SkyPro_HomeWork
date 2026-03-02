import pandas as pd


def read_data_csv(
    csv_path: str,
) -> list:
    """ Возвращает список словарей из csv """
    try:
        df = pd.read_csv(csv_path)
        return df.to_dict(orient='records')

    except (FileNotFoundError, pd.errors.EmptyDataError):
        # Файла нет или он пустой — возвращаем пустой список
        return []
    except (pd.errors.ParserError, UnicodeDecodeError):
        # Файл поврежден или кодировка не та
        return []
    except Exception as e:
        # На всякий случай ловим остальные критические ошибки
        print(f"Произошла непредвиденная ошибка: {e}")
        return []


def read_data_excel(
    excel_path: str,
) -> list:
    """ Возвращает список словарей из excel """
    try:
        df = pd.read_excel(excel_path)
        return df.to_dict(orient='records')
    except (FileNotFoundError, TypeError, ValueError):
        return []
    except Exception as e:
        # На всякий случай ловим остальные критические ошибки
        print(f"Произошла непредвиденная ошибка: {e}")
        return []
