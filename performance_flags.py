
import pandas as pd

# Load regional and monthly metrics
regional = pd.read_csv("regional_metrics.csv")
monthly = pd.read_csv("monthly_metrics.csv")

# Calculate overall average sales
average_sales = regional["total_sales"].mean()

# Flag regions with below-average sales
regional["low_sales_flag"] = (
    regional["total_sales"] < average_sales
)

# Calculate month-over-month sales growth
monthly = monthly.sort_values(["region", "month"])

monthly["sales_growth_pct"] = (
    monthly.groupby("region")["total_sales"]
    .pct_change() * 100
)

# Flag regions with a sales drop greater than 20%
monthly["sales_drop_flag"] = (
    monthly["sales_growth_pct"] < -20
)

# Save performance flags
regional.to_csv("regional_performance_flags.csv", index=False)
monthly.to_csv("monthly_performance_flags.csv", index=False)

print("Performance flags generated successfully!")

print("\nRegional performance flags:")
print(
    regional[
        ["region", "total_sales", "low_sales_flag"]
    ].to_string(index=False)
)

print("\nMonthly sales drop flags:")
print(
    monthly[
        ["region", "month", "sales_growth_pct", "sales_drop_flag"]
    ].to_string(index=False)
)