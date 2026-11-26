-- Snowflake: stage-to-stage funnel leakage and time-in-stage.
-- Read-only template. Export the result set; the skill narrates it — it does not
-- execute SQL.

WITH stage_events AS (
    SELECT
        opportunity_id,
        stage_name,
        MIN(stage_entered_at) AS stage_entered_at,
        MAX(stage_exited_at)  AS stage_exited_at
    FROM ANALYTICS.FCT_OPPORTUNITY_STAGE_HISTORY
    GROUP BY opportunity_id, stage_name
),
funnel AS (
    SELECT '01_qualification' AS stage_name, opportunity_id, stage_entered_at, stage_exited_at FROM stage_events
    UNION ALL
    SELECT '02_discovery',    opportunity_id, stage_entered_at, stage_exited_at FROM stage_events
    UNION ALL
    SELECT '03_proposal',     opportunity_id, stage_entered_at, stage_exited_at FROM stage_events
    UNION ALL
    SELECT '04_negotiation',  opportunity_id, stage_entered_at, stage_exited_at FROM stage_events
    UNION ALL
    SELECT '05_closed_won',   opportunity_id, stage_entered_at, stage_exited_at FROM stage_events
)
SELECT
    stage_name,
    COUNT(DISTINCT opportunity_id) AS deals_entered,
    DATEDIFF('day', MIN(stage_entered_at), MAX(stage_entered_at)) AS window_days,
    ROUND(AVG(DATEDIFF('day', stage_entered_at, stage_exited_at)), 1) AS avg_days_in_stage
FROM funnel
GROUP BY stage_name
ORDER BY stage_name;
