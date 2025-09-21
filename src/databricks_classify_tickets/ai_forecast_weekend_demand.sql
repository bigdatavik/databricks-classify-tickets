-- 🗓️ AI Forecast: Weekend vs Weekday Demand
-- Business Value: Predict weekend support needs for staffing and on-call planning

WITH daily_demand_pattern AS (
  SELECT
    DATE(created_date) AS ds,
    CASE 
      WHEN dayofweek(created_date) IN (1, 7) THEN 'Weekend'
      ELSE 'Weekday'
    END AS day_type,
    COUNT(ticket_id) AS demand_count
  FROM quickstart_catalog_vkm_external.classify_tickets.raw_tickets
  WHERE created_date IS NOT NULL
  GROUP BY DATE(created_date), 
    CASE 
      WHEN dayofweek(created_date) IN (1, 7) THEN 'Weekend'
      ELSE 'Weekday'
    END
  ORDER BY ds, day_type
),
max_date AS (
  SELECT MAX(ds) AS last_date FROM daily_demand_pattern
),
horizon_date AS (
  SELECT DATE_ADD(last_date, 7) AS horizon FROM max_date
)
SELECT 
  'Weekend vs Weekday Demand Forecast' as forecast_type,
  'Next 7 Days' as forecast_period,
  day_type,
  *
FROM ai_forecast(
  TABLE(daily_demand_pattern),
  horizon => (SELECT horizon FROM horizon_date),
  time_col => 'ds',
  value_col => 'demand_count',
  group_col => 'day_type'
);
