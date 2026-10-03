
import pandas as pd

# Load regional and monthly performance data
regional = pd.read_csv("regional_metrics.csv")
monthly = pd.read_csv("monthly_metrics.csv")

insights = []

# Overall sales leader
top_region = regional.loc[regional["total_sales"].idxmax()]
insights.append(
    f"{top_region['region']} recorded the highest total sales "
    f"of Rs. {top_region['total_sales']:,.2f}."
)

# Lowest sales region
low_region = regional.loc[regional["total_sales"].idxmin()]
insights.append(
    f"{low_region['region']} recorded the lowest total sales "
    f"of Rs. {low_region['total_sales']:,.2f}."
)

# Highest profit margin
best_margin = regional.loc[regional["profit_margin_pct"].idxmax()]
insights.append(
    f"{best_margin['region']} had the highest profit margin "
    f"at {best_margin['profit_margin_pct']:.2f}%."
)

# Largest monthly sales increase or decrease
monthly = monthly.sort_values(["region", "month"])
monthly["sales_growth_pct"] = (
    monthly.groupby("region")["total_sales"].pct_change() * 100
)

valid_growth = monthly.dropna(subset=["sales_growth_pct"])

if not valid_growth.empty:
    largest_increase = valid_growth.loc[
        valid_growth["sales_growth_pct"].idxmax()
    ]
    largest_drop = valid_growth.loc[
        valid_growth["sales_growth_pct"].idxmin()
    ]

    insights.append(
        f"{largest_increase['region']} had the largest month-over-month "
        f"sales increase of {largest_increase['sales_growth_pct']:.2f}% "
        f"in {largest_increase['month']}."
    )

    insights.append(
        f"{largest_drop['region']} had the largest month-over-month "
        f"sales decrease of {abs(largest_drop['sales_growth_pct']):.2f}% "
        f"in {largest_drop['month']}."
    )

# Save insights
with open("regional_insights.txt", "w", encoding="utf-8") as file:
    file.write("PHARMEASY REGIONAL PERFORMANCE INSIGHTS\n")
    file.write("=" * 45 + "\n\n")

    for number, insight in enumerate(insights, start=1):
        file.write(f"{number}. {insight}\n\n")

print("Insights generated successfully!\n")

for number, insight in enumerate(insights, start=1):
    print(f"{number}. {insight}")