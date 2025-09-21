-- 📊 AI Forecast: Ticket Volume Trends
-- Business Value: Predict daily ticket volumes for resource planning and capacity management

WITH daily_ticket_counts AS (
  SELECT
    DATE(created_date) AS ds,
    COUNT(ticket_id) AS ticket_count
  FROM quickstart_catalog_vkm_external.classify_tickets.raw_tickets
  WHERE created_date IS NOT NULL
  GROUP BY DATE(created_date)
  ORDER BY ds
),
max_date AS (
  SELECT MAX(ds) AS last_date FROM daily_ticket_counts
),
horizon_date AS (
  SELECT DATE_ADD(last_date, 7) AS horizon FROM max_date
)
SELECT 
  'Ticket Volume Forecast' as forecast_type,
  'Next 7 Days' as forecast_period,
  *
FROM ai_forecast(
  TABLE(daily_ticket_counts),
  horizon => (SELECT horizon FROM horizon_date),
  time_col => 'ds',
  value_col => 'ticket_count'
);
