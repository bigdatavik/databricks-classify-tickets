-- 🚨 AI Forecast: Urgent Ticket Trends
-- Business Value: Predict urgent ticket volumes to ensure adequate emergency response capacity

WITH daily_urgent_counts AS (
  SELECT
    DATE(created_date) AS ds,
    COUNT(CASE WHEN priority = '1 - Critical' THEN 1 END) AS urgent_count
  FROM quickstart_catalog_vkm_external.classify_tickets.raw_tickets
  WHERE created_date IS NOT NULL
  GROUP BY DATE(created_date)
  ORDER BY ds
),
max_date AS (
  SELECT MAX(ds) AS last_date FROM daily_urgent_counts
),
horizon_date AS (
  SELECT DATE_ADD(last_date, 7) AS horizon FROM max_date
)
SELECT 
  'Urgent Tickets Forecast' as forecast_type,
  'Next 7 Days' as forecast_period,
  *
FROM ai_forecast(
  TABLE(daily_urgent_counts),
  horizon => (SELECT horizon FROM horizon_date),
  time_col => 'ds',
  value_col => 'urgent_count'
);
