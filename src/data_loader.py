import pandas as pd
from config import ONLINE_RETAIL_FILE, ONLINE_RETAIL_FULL_CSV

def load_online_retail_excel() -> dict:
    """
    Load all sheets from the Online Retail II Excel file.
    Returns a dictionary of DataFrames.
    """
    sheets = pd.read_excel(
        ONLINE_RETAIL_FILE,
        sheet_name=None,
        engine="openpyxl"
    )
    return sheets


def merge_online_retail_sheets() -> pd.DataFrame:
    sheets = load_online_retail_excel()

    df_list = []
    for sheet_name, df in sheets.items():
        df["source_sheet"] = sheet_name
        df_list.append(df)

    merged_df = pd.concat(df_list, ignore_index=True)
    return merged_df


def save_merged_online_retail() -> pd.DataFrame:
    merged_df = merge_online_retail_sheets()
    ONLINE_RETAIL_FULL_CSV.parent.mkdir(parents=True, exist_ok=True)
    merged_df.to_csv(ONLINE_RETAIL_FULL_CSV, index=False)
    return merged_df


if __name__ == "__main__":
    df = save_merged_online_retail()
    print("Merged shape:", df.shape)
    print(df.head())