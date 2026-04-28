from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_RAW = PROJECT_ROOT / "data" / "raw"
DATA_INTERIM = PROJECT_ROOT / "data" / "interim"
DATA_PROCESSED = PROJECT_ROOT / "data" / "processed"

ONLINE_RETAIL_FILE = DATA_RAW / "online_retail_II.xlsx"

ONLINE_RETAIL_FULL_CSV = DATA_INTERIM / "online_retail_full.csv"
ONLINE_RETAIL_CLEAN_CSV = DATA_PROCESSED / "online_retail_clean.csv"
RFM_TABLE_CSV = DATA_PROCESSED / "customer_rfm.csv"