
import sqlite3
import pandas as pd

# Load normalized dataset
df = pd.read_csv("pharmeasy_orders_normalized.csv")

# Connect to SQLite database
conn = sqlite3.connect("pharmeasy.db")

# Update database with normalized data
df.to_sql("orders", conn, if_exists="replace", index=False)

# Calculate regional performance metrics
query = """
SELECT
    region,
    COUNT(order_id) AS total_orders,
    SUM(quantity) AS total_quantity,
    ROUND(SUM(sales_inr), 2) AS total_sales,
    ROUND(SUM(profit_inr), 2) AS total_profit,
    ROUND(
        SUM(profit_inr) * 100.0 / NULLIF(SUM(sales_inr), 0),
        2
    ) AS profit_margin_pct
FROM orders
GROUP BY region
ORDER BY total_sales DESC;
"""

# Execute query
metrics = pd.read_sql_query(query, conn)

# Save regional metrics
metrics.to_csv("regional_metrics.csv", index=False)

print("Regional metrics calculated successfully!")
print(metrics.to_string(index=False))

conn.close()