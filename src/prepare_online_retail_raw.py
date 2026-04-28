from pathlib import Path
import pandas as pd

RAW_PATH = Path("data/raw/online_retail_II.xlsx")
OUTPUT_PATH = Path("data/processed/online_retail_full.csv")

def load_and_concat_online_retail() -> pd.DataFrame:
    sheets = pd.read_excel(RAW_PATH, sheet_name=None, engine="openpyxl")

    df_list = []
    for sheet_name, df in sheets.items():
        df["source_sheet"] = sheet_name
        df_list.append(df)

    full_df = pd.concat(df_list, ignore_index=True)
    return full_df

def main():
    df = load_and_concat_online_retail()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print(f"Saved merged dataset to: {OUTPUT_PATH}")
    print("Shape:", df.shape)
    print(df.head())

if __name__ == "__main__":
    main()