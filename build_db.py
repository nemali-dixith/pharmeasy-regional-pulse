
import sqlite3
from pathlib import Path
import pandas as pd

# Project root directory
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

DB_FILE = BASE_DIR / "pharmeasy.db"

# Possible dataset locations
POSSIBLE_FILES = [
    BASE_DIR / "pharmeasy_orders_normalized.csv",
    DATA_DIR / "pharmeasy_orders_normalized.csv",
    BASE_DIR / "pharmeasy_orders_clean.csv",
    DATA_DIR / "pharmeasy_orders_clean.csv",
]


def load_dataset():
    for file_path in POSSIBLE_FILES:
        if file_path.exists():
            print(f"Loading dataset: {file_path}")
            return pd.read_csv(file_path)

    raise FileNotFoundError(
        "Dataset not found. Checked these locations:\n"
        + "\n".join(str(path) for path in POSSIBLE_FILES)
    )


def build_database():
    df = load_dataset()

    required_columns = [
        "order_id",
        "order_date",
        "region",
        "category",
        "product",
        "quantity",
        "sales_inr",
        "profit_inr"
    ]

    missing_columns = [
        col for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    if df.empty:
        raise ValueError("Dataset is empty.")

    # Normalize region names
    df["region"] = (
        df["region"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    # Store data in SQLite
    with sqlite3.connect(DB_FILE) as conn:
        df.to_sql(
            "orders",
            conn,
            if_exists="replace",
            index=False
        )

        total_records = pd.read_sql_query(
            "SELECT COUNT(*) AS total FROM orders",
            conn
        ).iloc[0]["total"]

        columns = pd.read_sql_query(
            "PRAGMA table_info(orders)",
            conn
        )

        regions = pd.read_sql_query(
            """
            SELECT DISTINCT region
            FROM orders
            ORDER BY region
            """,
            conn
        )

    print("\nDatabase created successfully!")
    print(f"Database location: {DB_FILE}")
    print(f"Total records stored: {total_records}")
    print(f"Total columns: {len(columns)}")
    print(f"Column names: {columns['name'].tolist()}")
    print(f"Distinct regions: {len(regions)}")
    print("\nRegion names:")
    print(regions.to_string(index=False))

    if total_records != len(df):
        raise ValueError("Database record count mismatch!")

    print("\nDatabase verification passed!")


if __name__ == "__main__":
    build_database()