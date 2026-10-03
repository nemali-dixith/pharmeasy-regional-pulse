
import os
import pandas as pd

# Required output files
required_files = [
    "pharmeasy_orders_normalized.csv",
    "regional_metrics.csv",
    "monthly_metrics.csv",
    "regional_performance_flags.csv",
    "monthly_performance_flags.csv",
    "regional_insights.txt",
    "regional_review_memo.txt"
]

# Check whether all required files exist
missing_files = [
    file for file in required_files
    if not os.path.exists(file)
]

# Load datasets
regional = pd.read_csv("regional_metrics.csv")
monthly = pd.read_csv("monthly_metrics.csv")
normalized = pd.read_csv("pharmeasy_orders_normalized.csv")

# Review checks
checks = {
    "All required files exist": len(missing_files) == 0,
    "Normalized dataset has no missing values": normalized.isnull().sum().sum() == 0,
    "Normalized dataset has no duplicate rows": normalized.duplicated().sum() == 0,
    "Exactly 9 standard regions": regional["region"].nunique() == 9,
    "Monthly data has 27 records": len(monthly) == 27,
    "Regional metrics have no missing values": regional.isnull().sum().sum() == 0
}

# Print review results
print("PHARMEASY REGIONAL PULSE - REVIEW GATE")
print("=" * 45)

for check, passed in checks.items():
    status = "PASS" if passed else "FAIL"
    print(f"{check}: {status}")

if missing_files:
    print("\nMissing files:")
    for file in missing_files:
        print("-", file)

# Final review decision
if all(checks.values()):
    decision = "APPROVED"
else:
    decision = "NEEDS REVIEW"

print("\nFinal review decision:", decision)

# Save review report
with open("review_report.txt", "w", encoding="utf-8") as file:
    file.write("PHARMEASY REGIONAL PULSE - REVIEW REPORT\n")
    file.write("=" * 45 + "\n\n")

    for check, passed in checks.items():
        status = "PASS" if passed else "FAIL"
        file.write(f"{check}: {status}\n")

    file.write(f"\nFinal review decision: {decision}\n")

print("\nReview report saved successfully!")