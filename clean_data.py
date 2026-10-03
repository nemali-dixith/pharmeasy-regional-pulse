
import pandas as pd
from pathlib import Path

# File paths
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_FILE = BASE_DIR / "pharmeasy_orders_raw.csv"
CLEAN_FILE = BASE_DIR / "pharmeasy_orders_clean.csv"


# Validate dataset schema
def validate_schema(df):
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
            f"Missing required columns: {missing_columns}"
        )

    if df.empty:
        raise ValueError("Dataset is empty.")

    print("Schema validation passed!")
    return True


# Load raw dataset
df = pd.read_csv(RAW_FILE)

# Validate before cleaning
validate_schema(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Handle missing category values
df["category"] = df["category"].fillna("Unknown")

# Handle missing profit values
df["profit_inr"] = df["profit_inr"].fillna(0)

# Save cleaned dataset
df.to_csv(CLEAN_FILE, index=False)

# Final report
print("\nCleaning completed successfully!")
print("Cleaned dataset shape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum())