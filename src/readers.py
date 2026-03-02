import pandas as pd


def read_data_csv(
    csv_path: str,
) -> list:
    df = pd.read_csv(csv_path)
    return df.to_dict(orient='records')

def read_data_excel(
    excel_path: str,
) -> list:
    df = pd.read_excel(excel_path)
    return df.to_dict(orient='records')
