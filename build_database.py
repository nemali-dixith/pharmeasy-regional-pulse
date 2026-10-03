
import sqlite3
from pathlib import Path

import pandas as pd

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
CLEAN_FILE = BASE_DIR / "pharmeasy_orders_clean.csv"
DB_FILE = BASE_DIR / "pharmeasy.db"


def build_database():
    # Check whether cleaned dataset exists
    if not CLEAN_FILE.exists():
        raise FileNotFoundError(
            f"Cleaned dataset not found: {CLEAN_FILE}"
        )

    # Load cleaned dataset
    df = pd.read_csv(CLEAN_FILE)

    if df.empty:
        raise ValueError("Cleaned dataset is empty.")

    # Connect to SQLite database
    with sqlite3.connect(DB_FILE) as conn:
        # Store data in SQLite
        df.to_sql(
            "orders",
            conn,
            if_exists="replace",
            index=False
        )

        # Verify record count
        result = pd.read_sql_query(
            "SELECT COUNT(*) AS total_orders FROM orders",
            conn
        )

        total_records = int(
            result.iloc[0]["total_orders"]
        )

        # Verify table columns
        columns = pd.read_sql_query(
            "PRAGMA table_info(orders)",
            conn
        )

    print("Database created successfully!")
    print("Database location:", DB_FILE)
    print("Total records stored:", total_records)
    print("Total columns:", len(columns))
    print("Column names:", columns["name"].tolist())

    if total_records != len(df):
        raise ValueError(
            "Database record count does not match CSV."
        )

    print("Database verification passed!")


if __name__ == "__main__":
    build_database()