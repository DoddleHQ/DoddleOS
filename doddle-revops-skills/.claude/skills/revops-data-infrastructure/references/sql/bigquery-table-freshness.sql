-- BigQuery: table freshness from metadata, plus row-count drift.
-- Read-only. Export to JSON and feed it to `drev data-profile`.

SELECT
    project_id,
    table_id,
    creation_time,
    last_modified_time,
    DATE_DIFF(CURRENT_TIMESTAMP(), last_modified_time, HOUR) AS hours_since_modified,
    row_count,
    size_bytes
FROM `region-us`.INFORMATION_SCHEMA.TABLE_STORAGE
ORDER BY last_modified_time ASC;

-- Canonical identity coverage for a customer dimension.
-- SELECT
--     COUNT(*) AS total_records,
--     COUNTIF(canonical_id IS NOT NULL) AS mapped_records,
--     SAFE_DIVIDE(COUNTIF(canonical_id IS NOT NULL), COUNT(*)) AS identity_match_rate
-- FROM `project`.dim_customers;
