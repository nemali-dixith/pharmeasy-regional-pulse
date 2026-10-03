import pandas as pd

# Load cleaned dataset
df = pd.read_csv("pharmeasy_orders_clean.csv")

# Validation checks
print("Dataset shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())
print("Negative quantities:", (df["quantity"] < 0).sum())
print("Negative sales:", (df["sales_inr"] < 0).sum())
print("Negative profits:", (df["profit_inr"] < 0).sum())

# Date validation
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
print("Invalid dates:", df["order_date"].isnull().sum())