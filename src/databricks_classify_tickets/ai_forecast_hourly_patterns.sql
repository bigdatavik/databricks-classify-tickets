-- ⏰ AI Forecast: Hourly Ticket Patterns
-- Business Value: Predict peak hours for optimal staff scheduling and capacity planning

WITH hourly_ticket_counts AS (
  SELECT
    DATE(created_date) AS ds,
    HOUR(created_timestamp) AS hour_of_day,
    COUNT(ticket_id) AS hourly_count
  FROM quickstart_catalog_vkm_external.classify_tickets.raw_tickets
  WHERE created_date IS NOT NULL
    AND created_timestamp IS NOT NULL
  GROUP BY DATE(created_date), HOUR(created_timestamp)
  ORDER BY ds, hour_of_day
),
max_date AS (
  SELECT MAX(ds) AS last_date FROM hourly_ticket_counts
),
horizon_date AS (
  SELECT DATE_ADD(last_date, 1) AS horizon FROM max_date
)
SELECT 
  'Hourly Pattern Forecast' as forecast_type,
  'Next Day' as forecast_period,
  hour_of_day,
  *
FROM ai_forecast(
  TABLE(hourly_ticket_counts),
  horizon => (SELECT horizon FROM horizon_date),
  time_col => 'ds',
  value_col => 'hourly_count',
  group_col => 'hour_of_day'
);
