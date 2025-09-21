-- 👥 AI Forecast: Customer Impact Trends
-- Business Value: Predict customer-facing issues to prioritize support and communication

WITH daily_customer_impact AS (
  SELECT
    DATE(created_date) AS ds,
    CASE 
      WHEN LOWER(description) LIKE '%customer%' OR LOWER(description) LIKE '%user%' THEN 'Customer Facing'
      WHEN LOWER(description) LIKE '%internal%' OR LOWER(description) LIKE '%admin%' THEN 'Internal'
      WHEN LOWER(description) LIKE '%urgent%' OR LOWER(description) LIKE '%asap%' THEN 'High Impact'
      ELSE 'Standard'
    END AS impact_level,
    COUNT(ticket_id) AS impact_count
  FROM quickstart_catalog_vkm_external.classify_tickets.raw_tickets
  WHERE created_date IS NOT NULL
  GROUP BY DATE(created_date), 
    CASE 
      WHEN LOWER(description) LIKE '%customer%' OR LOWER(description) LIKE '%user%' THEN 'Customer Facing'
      WHEN LOWER(description) LIKE '%internal%' OR LOWER(description) LIKE '%admin%' THEN 'Internal'
      WHEN LOWER(description) LIKE '%urgent%' OR LOWER(description) LIKE '%asap%' THEN 'High Impact'
      ELSE 'Standard'
    END
  ORDER BY ds, impact_level
),
max_date AS (
  SELECT MAX(ds) AS last_date FROM daily_customer_impact
),
horizon_date AS (
  SELECT DATE_ADD(last_date, 7) AS horizon FROM max_date
)
SELECT 
  'Customer Impact Forecast' as forecast_type,
  'Next 7 Days' as forecast_period,
  impact_level,
  *
FROM ai_forecast(
  TABLE(daily_customer_impact),
  horizon => (SELECT horizon FROM horizon_date),
  time_col => 'ds',
  value_col => 'impact_count',
  group_col => 'impact_level'
);
