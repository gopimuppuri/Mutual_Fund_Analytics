# Mutual Fund Analytics - Data Dictionary

## dim_fund

| Column Name   | Data Type | Description              | Source                 |
| ------------- | --------- | ------------------------ | ---------------------- |
| amfi_code     | TEXT      | Unique fund identifier   | fund_master.csv        |
| scheme_name   | TEXT      | Mutual fund scheme name  | fund_master.csv        |
| fund_house    | TEXT      | Asset Management Company | fund_master.csv        |
| category      | TEXT      | Fund category            | fund_master.csv        |
| risk_category | TEXT      | Risk level of fund       | scheme_performance.csv |

---

## fact_nav

| Column Name  | Data Type | Description             | Source          |
| ------------ | --------- | ----------------------- | --------------- |
| amfi_code    | TEXT      | Fund identifier         | nav_history.csv |
| date         | DATE      | NAV date                | nav_history.csv |
| nav          | REAL      | Net Asset Value         | nav_history.csv |
| daily_return | REAL      | Daily percentage return | Calculated      |

Formula:

daily_return = ((Today's NAV - Previous NAV) / Previous NAV) * 100

---

## fact_transactions

| Column Name        | Data Type | Description                | Source                    |
| ------------------ | --------- | -------------------------- | ------------------------- |
| investor_id        | TEXT      | Investor identifier        | investor_transactions.csv |
| transaction_date   | DATE      | Transaction date           | investor_transactions.csv |
| amfi_code          | TEXT      | Fund identifier            | investor_transactions.csv |
| transaction_type   | TEXT      | SIP / Lumpsum / Redemption | investor_transactions.csv |
| amount_inr         | REAL      | Transaction amount         | investor_transactions.csv |
| state              | TEXT      | Investor state             | investor_transactions.csv |
| city               | TEXT      | Investor city              | investor_transactions.csv |
| city_tier          | TEXT      | Tier of city               | investor_transactions.csv |
| age_group          | TEXT      | Investor age group         | investor_transactions.csv |
| gender             | TEXT      | Investor gender            | investor_transactions.csv |
| annual_income_lakh | REAL      | Annual income in lakhs     | investor_transactions.csv |
| payment_mode       | TEXT      | UPI / Cheque / Net Banking | investor_transactions.csv |
| kyc_status         | TEXT      | KYC verification status    | investor_transactions.csv |

---

## fact_performance

| Column Name        | Data Type | Description             | Source                 |
| ------------------ | --------- | ----------------------- | ---------------------- |
| amfi_code          | TEXT      | Fund identifier         | scheme_performance.csv |
| scheme_name        | TEXT      | Scheme name             | scheme_performance.csv |
| fund_house         | TEXT      | AMC name                | scheme_performance.csv |
| category           | TEXT      | Fund category           | scheme_performance.csv |
| plan               | TEXT      | Regular / Direct        | scheme_performance.csv |
| return_1yr_pct     | REAL      | 1 Year Return           | scheme_performance.csv |
| return_3yr_pct     | REAL      | 3 Year Return           | scheme_performance.csv |
| return_5yr_pct     | REAL      | 5 Year Return           | scheme_performance.csv |
| benchmark_3yr_pct  | REAL      | Benchmark Return        | scheme_performance.csv |
| alpha              | REAL      | Alpha Ratio             | scheme_performance.csv |
| beta               | REAL      | Beta Ratio              | scheme_performance.csv |
| sharpe_ratio       | REAL      | Sharpe Ratio            | scheme_performance.csv |
| sortino_ratio      | REAL      | Sortino Ratio           | scheme_performance.csv |
| std_dev_ann_pct    | REAL      | Standard Deviation      | scheme_performance.csv |
| max_drawdown_pct   | REAL      | Maximum Drawdown        | scheme_performance.csv |
| aum_crore          | REAL      | Assets Under Management | scheme_performance.csv |
| expense_ratio_pct  | REAL      | Expense Ratio           | scheme_performance.csv |
| morningstar_rating | INTEGER   | Rating out of 5         | scheme_performance.csv |
| risk_grade         | TEXT      | Risk classification     | scheme_performance.csv |
