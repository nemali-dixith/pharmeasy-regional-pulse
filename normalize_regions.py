import pandas as pd

# Load cleaned dataset and region master
df = pd.read_csv("pharmeasy_orders_clean.csv")
regions = pd.read_csv("regions_master.csv")

# Create a case-insensitive mapping
region_map = {
    region.strip().lower(): region
    for region in regions["region"]
}

# Normalize region names
df["region"] = (
    df["region"]
    .astype(str)
    .str.strip()
    .str.lower()
    .map(region_map)
    .fillna(df["region"])
)

# Save normalized dataset
df.to_csv("pharmeasy_orders_normalized.csv", index=False)

print("Region normalization completed!")
print("\nUnique regions after normalization:")
print(sorted(df["region"].unique()))