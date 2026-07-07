import os
import pandas as pd
import matplotlib.pyplot as plt

# Create output folders if they don't exist
os.makedirs("reports", exist_ok=True)
os.makedirs("charts", exist_ok=True)

# Load performance data
performance = pd.read_csv("data/processed/clean_performance.csv")

# Keep only rows with required values
recommend = performance.dropna(
    subset=[
        "return_3yr_pct",
        "sharpe_ratio",
        "expense_ratio_pct",
        "max_drawdown_pct"
    ]
).copy()

# Create Fund Score
recommend["Fund_Score"] = (
    recommend["return_3yr_pct"] * 0.40 +
    recommend["sharpe_ratio"] * 0.30 -
    recommend["expense_ratio_pct"] * 0.15 -
    recommend["max_drawdown_pct"] * 0.15
)

# Get Top 5 Funds
top5 = recommend.sort_values(
    "Fund_Score",
    ascending=False
).head(5)

# Save report
top5.to_csv("../reports/fund_recommendation.csv", index=False)

# Plot chart
plt.figure(figsize=(12, 6))

plt.barh(
    top5["scheme_name"],
    top5["Fund_Score"]
)

plt.gca().invert_yaxis()

plt.title("Top 5 Recommended Mutual Funds")
plt.xlabel("Fund Score")

plt.tight_layout()

plt.savefig(
    "../charts/top5_recommended_funds.png",
    dpi=300
)

plt.show()

print("\nTop 5 Recommended Funds\n")
print(
    top5[
        [
            "scheme_name",
            "fund_house",
            "category",
            "return_3yr_pct",
            "sharpe_ratio",
            "expense_ratio_pct",
            "Fund_Score"
        ]
    ]
)

print("\nFund Recommendation Report Saved Successfully!")