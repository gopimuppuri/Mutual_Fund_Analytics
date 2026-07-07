import pandas as pd
from sqlalchemy import create_engine
import os

# Database connection
engine = create_engine("sqlite:///data/db/bluestock_mf.db")

files = {
    "dim_fund": "data/processed/clean_fund_master.csv",
    "fact_nav": "data/processed/clean_nav.csv",
    "fact_transactions": "data/processed/clean_transactions.csv",
    "fact_performance": "data/processed/clean_performance.csv",
    "fact_portfolio": "data/processed/clean_portfolio_holdings.csv",
    "fact_sip_industry": "data/processed/clean_monthly_sip_inflows.csv",
    "fact_aum": "data/processed/clean_aum_by_fund_house.csv"
}

print("=" * 60)
print("Bluestock Mutual Fund ETL Pipeline")
print("=" * 60)

for table_name, file_path in files.items():
    print(table_name, "->", file_path)
    if os.path.exists(file_path):

        print(f"Loading {os.path.basename(file_path)}...")

        df = pd.read_csv(file_path)

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(f"Loaded into table: {table_name}")

    else:

        print(f"File not found: {file_path}")

print("=" * 60)
print("ETL Pipeline Completed Successfully")
print("=" * 60)