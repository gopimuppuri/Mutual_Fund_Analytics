
SELECT * FROM dim_fund;
SELECT * FROM fact_nav;
SELECT * FROM fact_performance;
SELECT * FROM fact_transactions;
SELECT * FROM dim_date;
SELECT * FROM fact_aum;


SELECT COUNT(*) FROM dim_date;
SELECT COUNT(*) FROM fact_aum;
SELECT COUNT(*) FROM fact_transactions;
SELECT COUNT(*) FROM fact_performance;
SELECT COUNT(*) FROM fact_nav;
SELECT COUNT(*) FROM dim_fund;





-- 1. Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5 ;

-- 2.Average NAV Per Month

SELECT strftime ('%Y-%m', date) AS month,
    ROUND(AVG(nav),2) AS avg_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

 
-- 3.SIP Inflow YoY Growth
SELECT strftime ('%Y', transaction_date) AS year,
    SUM(amount_inr) AS sip_inflow
FROM fact_transactions
WHERE transaction_type='SIP'
GROUP BY year;

-- 4. Transactions by State
SELECT state,
    COUNT(*) AS transactions
FROM fact_transactions
GROUP BY state
ORDER BY transactions DESC;


-- 5: Funds with Expense Ratio < 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- 6. Total Number of Transactions
SELECT COUNT(*) AS total_transactions
FROM fact_transactions;

-- 7. Fund Count by Category
SELECT category, COUNT(*) AS fund_count
FROM fact_performance
GROUP BY category
ORDER BY fund_count DESC;


-- 8. Total SIP Transactions
SELECT COUNT(*) AS sip_transactions
FROM fact_transactions
WHERE transaction_type = 'SIP';

-- 9. Average Expense Ratio by Category
SELECT category,
    ROUND(AVG(expense_ratio_pct), 2) AS avg_expense_ratio
FROM fact_performance
GROUP BY category;


-- 10. Maximum NAV
SELECT MAX(nav)
FROM fact_nav;



