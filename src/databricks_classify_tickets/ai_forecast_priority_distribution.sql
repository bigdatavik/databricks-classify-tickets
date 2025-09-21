-- 📈 AI Forecast: Priority Distribution Trends
-- Business Value: Predict priority mix to plan resource allocation and SLA management

WITH daily_priority_counts AS (
  SELECT
    DATE(created_date) AS ds,
    priority,
    COUNT(ticket_id) AS priority_count
  FROM quickstart_catalog_vkm_external.classify_tickets.raw_tickets
  WHERE created_date IS NOT NULL
  GROUP BY DATE(created_date), priority
  ORDER BY ds, priority
),
max_date AS (
  SELECT MAX(ds) AS last_date FROM daily_priority_counts
),
horizon_date AS (
  SELECT DATE_ADD(last_date, 7) AS horizon FROM max_date
)
SELECT 
  'Priority Distribution Forecast' as forecast_type,
  'Next 7 Days' as forecast_period,
  priority,
  *
FROM ai_forecast(
  TABLE(daily_priority_counts),
  horizon => (SELECT horizon FROM horizon_date),
  time_col => 'ds',
  value_col => 'priority_count',
  group_col => 'priority'
);
