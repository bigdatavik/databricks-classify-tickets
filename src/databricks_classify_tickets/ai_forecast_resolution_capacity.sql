-- ⚡ AI Forecast: Resolution Capacity Planning
-- Business Value: Predict ticket resolution capacity needs for staffing and SLA management

WITH daily_resolution_metrics AS (
  SELECT
    DATE(created_date) AS ds,
    COUNT(ticket_id) AS total_tickets,
    COUNT(CASE WHEN state = 'New' THEN 1 END) AS new_tickets,
    COUNT(CASE WHEN state = 'In Progress' THEN 1 END) AS in_progress_tickets,
    COUNT(CASE WHEN state = 'Assigned' THEN 1 END) AS assigned_tickets
  FROM quickstart_catalog_vkm_external.classify_tickets.raw_tickets
  WHERE created_date IS NOT NULL
  GROUP BY DATE(created_date)
  ORDER BY ds
),
max_date AS (
  SELECT MAX(ds) AS last_date FROM daily_resolution_metrics
),
horizon_date AS (
  SELECT DATE_ADD(last_date, 7) AS horizon FROM max_date
)
SELECT 
  'Resolution Capacity Forecast' as forecast_type,
  'Next 7 Days' as forecast_period,
  *
FROM ai_forecast(
  TABLE(daily_resolution_metrics),
  horizon => (SELECT horizon FROM horizon_date),
  time_col => 'ds',
  value_col => ARRAY('total_tickets', 'new_tickets', 'in_progress_tickets', 'assigned_tickets')
);
