
import pandas as pd

# Load generated insights and performance data
regional = pd.read_csv("regional_metrics.csv")
monthly = pd.read_csv("monthly_metrics.csv")

# Identify key regions
top_region = regional.loc[regional["total_sales"].idxmax()]
low_region = regional.loc[regional["total_sales"].idxmin()]
best_margin = regional.loc[regional["profit_margin_pct"].idxmax()]

# Calculate monthly sales growth
monthly = monthly.sort_values(["region", "month"])
monthly["sales_growth_pct"] = (
    monthly.groupby("region")["total_sales"].pct_change() * 100
)

valid_growth = monthly.dropna(subset=["sales_growth_pct"])
largest_drop = valid_growth.loc[
    valid_growth["sales_growth_pct"].idxmin()
]

# Create business review memo
memo = f"""
PHARMEASY REGIONAL PULSE
REGIONAL PERFORMANCE REVIEW
April–June 2026

1. EXECUTIVE SUMMARY

The regional performance analysis covers 9 regions
and 3 months of order data.

{top_region['region']} recorded the highest total sales
of Rs. {top_region['total_sales']:,.2f}.

{low_region['region']} recorded the lowest total sales
of Rs. {low_region['total_sales']:,.2f}.

2. KEY FINDINGS

• Sales leader:
  {top_region['region']} with Rs. {top_region['total_sales']:,.2f}
  in total sales.

• Lowest total sales:
  {low_region['region']} with Rs. {low_region['total_sales']:,.2f}.

• Highest profit margin:
  {best_margin['region']} at
  {best_margin['profit_margin_pct']:.2f}%.

• Largest monthly sales decline:
  {largest_drop['region']} experienced a
  {abs(largest_drop['sales_growth_pct']):.2f}% decline
  in {largest_drop['month']} compared with the previous month.

3. RECOMMENDED REVIEW ACTIONS

• Review the sales trends and operational factors
  behind the largest monthly sales decline.

• Investigate the practices and product mix associated
  with regions reporting higher profit margins.

• Examine sales opportunities in regions with lower
  total sales before deciding on corrective actions.

4. REVIEW NOTE

These findings are based on the available order data
for April–June 2026. The analysis identifies patterns
but does not establish their underlying causes.

Further business context is required before
implementing operational changes.
"""

# Save memo
with open("regional_review_memo.txt", "w", encoding="utf-8") as file:
    file.write(memo)

print("Business review memo generated successfully!")
print(memo)