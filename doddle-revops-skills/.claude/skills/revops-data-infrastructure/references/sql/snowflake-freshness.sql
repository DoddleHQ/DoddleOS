-- Snowflake: table freshness and row-count drift.
-- Read-only. Run in a read-only role; export results and feed them to
-- `drev data-profile --warehouse-export`.

SELECT
    table_schema,
    table_name,
    last_alter,
    row_count,
    last_load_time,
    DATEDIFF('hour', last_load_time, CURRENT_TIMESTAMP()) AS hours_since_load
FROM SNOWFLAKE.ACCOUNT_USAGE.TABLES
WHERE deleted IS NULL
  AND table_type = 'BASE TABLE'
ORDER BY last_load_time NULLS FIRST;

-- Duplicate-key check on the opportunity fact table.
-- SELECT
--     opportunity_id,
--     COUNT(*) AS rows_per_key
-- FROM ANALYTICS.FCT_OPPORTUNITIES
-- GROUP BY opportunity_id
-- HAVING COUNT(*) > 1
-- ORDER BY rows_per_key DESC
-- LIMIT 100;
