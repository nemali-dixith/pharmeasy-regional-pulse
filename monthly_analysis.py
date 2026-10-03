
import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("pharmeasy.db")

# Calculate monthly sales and profit for each region
query = """
SELECT
    region,
    strftime('%Y-%m', order_date) AS month,
    COUNT(order_id) AS total_orders,
    ROUND(SUM(sales_inr), 2) AS total_sales,
    ROUND(SUM(profit_inr), 2) AS total_profit
FROM orders
GROUP BY region, month
ORDER BY region, month;
"""

# Execute query
monthly_metrics = pd.read_sql_query(query, conn)

# Save monthly metrics
monthly_metrics.to_csv("monthly_metrics.csv", index=False)

print("Monthly analysis completed successfully!")
print(monthly_metrics.to_string(index=False))

conn.close()