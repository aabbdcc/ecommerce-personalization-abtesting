import pandas as pd
from config import ONLINE_RETAIL_FULL_CSV, ONLINE_RETAIL_CLEAN_CSV

def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df


def clean_online_retail(df: pd.DataFrame) -> pd.DataFrame:
    df = standardize_columns(df)

    # Identify key columns dynamically
    invoice_col = [c for c in df.columns if "invoice" in c][0]
    date_col = [c for c in df.columns if "date" in c][0]
    price_col = [c for c in df.columns if "price" in c][0]

    df[invoice_col] = df[invoice_col].astype(str)
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

    # cancellation invoices usually start with C
    df["is_cancellation"] = df[invoice_col].str.lower().str.startswith("c")

    # Keep only valid positive orders for analytics
    df = df[~df["is_cancellation"]]
    df = df[df["customer_id"].notna()]
    df = df[df["quantity"] > 0]
    df = df[df[price_col] > 0]
    df = df[df[date_col].notna()]

    df["customer_id"] = df["customer_id"].astype(str)
    df["sales_amount"] = df["quantity"] * df[price_col]

    # Rename columns into a stable schema
    rename_map = {
        invoice_col: "invoice_no",
        date_col: "invoice_date",
        price_col: "unit_price"
    }
    df = df.rename(columns=rename_map)

    return df


def save_clean_online_retail() -> pd.DataFrame:
    df = pd.read_csv(ONLINE_RETAIL_FULL_CSV)
    clean_df = clean_online_retail(df)

    ONLINE_RETAIL_CLEAN_CSV.parent.mkdir(parents=True, exist_ok=True)
    clean_df.to_csv(ONLINE_RETAIL_CLEAN_CSV, index=False)
    return clean_df


if __name__ == "__main__":
    df = save_clean_online_retail()
    print("Clean shape:", df.shape)
    print(df.head())