-- 👥 AI Forecast: Team Workload Distribution
-- Business Value: Predict team workload to optimize resource allocation and prevent burnout

WITH daily_team_workload AS (
  SELECT
    DATE(created_date) AS ds,
    assignment_group,
    COUNT(ticket_id) AS team_ticket_count
  FROM quickstart_catalog_vkm_external.classify_tickets.raw_tickets
  WHERE created_date IS NOT NULL 
    AND assignment_group != 'Unassigned'
  GROUP BY DATE(created_date), assignment_group
  ORDER BY ds, assignment_group
),
max_date AS (
  SELECT MAX(ds) AS last_date FROM daily_team_workload
),
horizon_date AS (
  SELECT DATE_ADD(last_date, 7) AS horizon FROM max_date
)
SELECT 
  'Team Workload Forecast' as forecast_type,
  'Next 7 Days' as forecast_period,
  assignment_group,
  *
FROM ai_forecast(
  TABLE(daily_team_workload),
  horizon => (SELECT horizon FROM horizon_date),
  time_col => 'ds',
  value_col => 'team_ticket_count',
  group_col => 'assignment_group'
);
