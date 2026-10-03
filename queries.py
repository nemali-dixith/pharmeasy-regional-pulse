
import sqlite3
from pathlib import Path
import pandas as pd

# Project root folder
BASE_DIR = Path(__file__).resolve().parent
DB_FILE = BASE_DIR / "pharmeasy.db"


def run_queries():
    if not DB_FILE.exists():
        raise FileNotFoundError(
            f"Database not found: {DB_FILE}\n"
            "Please run build_db.py first."
        )

    with sqlite3.connect(DB_FILE) as conn:

        # 1. Overall business metrics
        overview_query = """
        SELECT
            COUNT(DISTINCT order_id) AS total_orders,
            ROUND(SUM(sales_inr), 2) AS total_sales_inr,
            ROUND(SUM(profit_inr), 2) AS total_profit_inr,
            ROUND(AVG(sales_inr), 2) AS average_sales_inr
        FROM orders;
        """

        overview = pd.read_sql_query(overview_query, conn)

        # 2. Region-wise business metrics
        regional_query = """
        SELECT
            region,
            COUNT(DISTINCT order_id) AS total_orders,
            ROUND(SUM(sales_inr), 2) AS total_sales_inr,
            ROUND(SUM(profit_inr), 2) AS total_profit_inr,
            ROUND(AVG(sales_inr), 2) AS average_sales_inr
        FROM orders
        GROUP BY region
        ORDER BY total_sales_inr DESC;
        """

        regional = pd.read_sql_query(regional_query, conn)

        # 3. JOIN validation
        join_query = """
        SELECT
            o.region,
            COUNT(*) AS joined_records
        FROM orders AS o
        INNER JOIN (
            SELECT DISTINCT region
            FROM orders
        ) AS r
        ON o.region = r.region
        GROUP BY o.region
        ORDER BY o.region;
        """

        joined = pd.read_sql_query(join_query, conn)

        # 4. Source record counts for validation
        source_query = """
        SELECT
            region,
            COUNT(*) AS source_records
        FROM orders
        GROUP BY region
        ORDER BY region;
        """

        source = pd.read_sql_query(source_query, conn)

        # 5. Compare source and joined records
        join_valid = (
            source["region"].equals(joined["region"])
            and source["source_records"].equals(
                joined["joined_records"]
            )
        )

        source_total = int(source["source_records"].sum())
        joined_total = int(joined["joined_records"].sum())

        # 6. Display results
        print("\n========== OVERALL BUSINESS METRICS ==========")
        print(overview.to_string(index=False))

        print("\n========== REGION-WISE BUSINESS METRICS ==========")
        print(regional.to_string(index=False))

        print("\n========== JOIN VALIDATION DETAILS ==========")
        print(joined.to_string(index=False))

        print("\n========== VALIDATION RESULT ==========")
        if join_valid:
            print("PASS: JOIN preserved all source records.")
        else:
            print("FAIL: JOIN record counts do not match.")

        print(f"Total source records: {source_total}")
        print(f"Total joined records: {joined_total}")


if __name__ == "__main__":
    run_queries()