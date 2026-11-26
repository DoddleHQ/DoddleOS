-- BigQuery: monthly cohort retention matrix.
-- Read-only template. Export the result set and run `drev cohorts` on it, or read
-- it as the cohort input file.

WITH base AS (
    SELECT
        account_id,
        DATE_TRUNC(DATE(cohort_start), MONTH) AS cohort_month,
        DATE_TRUNC(DATE(period_start), MONTH) AS period_month,
        ANY_VALUE(TRUE)  AS is_active,
        SUM(SAFE_CAST(revenue AS FLOAT64)) AS revenue
    FROM `project`.fct_customer_periods
    GROUP BY account_id, cohort_month, period_month
),
indexed AS (
    SELECT
        account_id,
        cohort_month,
        period_month,
        is_active,
        revenue,
        ((EXTRACT(YEAR FROM period_month) - EXTRACT(YEAR FROM cohort_month)) * 12
         + EXTRACT(MONTH FROM period_month) - EXTRACT(MONTH FROM cohort_month)) AS period_index
    FROM base
)
SELECT
    cohort_month,
    period_index,
    COUNT(DISTINCT account_id) AS cohort_size,
    COUNT(DISTINCT IF(is_active, account_id, NULL)) AS active_accounts,
    SAFE_DIVIDE(COUNT(DISTINCT IF(is_active, account_id, NULL)), COUNT(DISTINCT account_id)) AS logo_retention,
    SUM(revenue) AS revenue
FROM indexed
WHERE period_index BETWEEN 0 AND 12
GROUP BY cohort_month, period_index
ORDER BY cohort_month, period_index;
