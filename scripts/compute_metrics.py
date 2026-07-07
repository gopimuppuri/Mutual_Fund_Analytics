import os
import numpy as np
import pandas as pd

# ==========================================================
# Create folders
# ==========================================================

os.makedirs("data/processed", exist_ok=True)

# ==========================================================
# Load NAV History
# ==========================================================

nav = pd.read_csv("data/processed/clean_nav.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(["amfi_code", "date"])

# ==========================================================
# Daily Return
# ==========================================================

nav["daily_return"] = (
    nav.groupby("amfi_code")["nav"]
       .pct_change()
)

# ==========================================================
# Load Fund Master
# ==========================================================

fund = pd.read_csv("data/processed/clean_fund_master.csv")

# ==========================================================
# Annual Risk Free Rate
# ==========================================================

RISK_FREE = 0.06

DAILY_RF = RISK_FREE / 252

# ==========================================================
# Metric Function
# ==========================================================

records = []

for code, df in nav.groupby("amfi_code"):

    df = df.dropna()

    if len(df) < 252:
        continue

    latest = df.iloc[-1]["nav"]

    # ----------------------------
    # Returns
    # ----------------------------

    ret1 = np.nan
    ret3 = np.nan
    ret5 = np.nan

    if len(df) >= 252:
        ret1 = (latest / df.iloc[-252]["nav"] - 1) * 100

    if len(df) >= 252 * 3:
        ret3 = (latest / df.iloc[-252 * 3]["nav"] - 1) * 100

    if len(df) >= 252 * 5:
        ret5 = (latest / df.iloc[-252 * 5]["nav"] - 1) * 100

    # ----------------------------
    # Std Deviation
    # ----------------------------

    std = df["daily_return"].std() * np.sqrt(252) * 100

    # ----------------------------
    # Sharpe
    # ----------------------------

    excess = df["daily_return"] - DAILY_RF

    if df["daily_return"].std() == 0:
        sharpe = np.nan
    else:
        sharpe = (
            excess.mean()
            / df["daily_return"].std()
        ) * np.sqrt(252)

    # ----------------------------
    # Sortino
    # ----------------------------

    downside = excess[excess < 0]

    if len(downside) == 0:
        sortino = np.nan
    else:
        sortino = (
            excess.mean()
            / downside.std()
        ) * np.sqrt(252)

    # ----------------------------
    # Max Drawdown
    # ----------------------------

    cumulative = (1 + df["daily_return"]).cumprod()

    rolling = cumulative.cummax()

    drawdown = cumulative / rolling - 1

    max_dd = drawdown.min() * 100

    records.append({

        "amfi_code": code,

        "return_1yr_pct": round(ret1,2),

        "return_3yr_pct": round(ret3,2),

        "return_5yr_pct": round(ret5,2),

        "benchmark_3yr_pct": np.nan,

        "alpha": np.nan,

        "beta": np.nan,

        "sharpe_ratio": round(sharpe,3),

        "sortino_ratio": round(sortino,3),

        "std_dev_ann_pct": round(std,2),

        "max_drawdown_pct": round(max_dd,2)

    })

# ==========================================================
# Metrics DataFrame
# ==========================================================

metrics = pd.DataFrame(records)

# ==========================================================
# Merge with Fund Master
# ==========================================================

performance = fund.merge(
    metrics,
    on="amfi_code",
    how="left"
)

# ==========================================================
# Placeholder Columns
# ==========================================================

performance["aum_crore"] = np.nan

performance["morningstar_rating"] = np.nan

performance["risk_grade"] = ""

performance["anomaly_flag"] = False

performance["expense_ratio_valid"] = (
    performance["expense_ratio_pct"] <= 2
)

# ==========================================================
# Save
# ==========================================================

performance.to_csv(
    "data/processed/clean_performance.csv",
    index=False
)

print("="*60)
print("Performance metrics created successfully")
print("="*60)

print(performance.head())