-- 🔧 AI Forecast: System-Specific Issue Trends
-- Business Value: Predict which systems will have issues to enable proactive maintenance

WITH daily_system_issues AS (
  SELECT
    DATE(created_date) AS ds,
    CASE 
      WHEN LOWER(description) LIKE '%website%' OR LOWER(description) LIKE '%web%' THEN 'Website'
      WHEN LOWER(description) LIKE '%api%' THEN 'API'
      WHEN LOWER(description) LIKE '%database%' OR LOWER(description) LIKE '%db%' THEN 'Database'
      WHEN LOWER(description) LIKE '%login%' OR LOWER(description) LIKE '%auth%' THEN 'Authentication'
      WHEN LOWER(description) LIKE '%monitor%' THEN 'Monitoring'
      WHEN LOWER(description) LIKE '%backup%' THEN 'Backup'
      WHEN LOWER(description) LIKE '%cloud%' THEN 'Cloud Infrastructure'
      WHEN LOWER(description) LIKE '%production%' THEN 'Production'
      ELSE 'Other'
    END AS system_type,
    COUNT(ticket_id) AS system_issue_count
  FROM quickstart_catalog_vkm_external.classify_tickets.raw_tickets
  WHERE created_date IS NOT NULL
  GROUP BY DATE(created_date), 
    CASE 
      WHEN LOWER(description) LIKE '%website%' OR LOWER(description) LIKE '%web%' THEN 'Website'
      WHEN LOWER(description) LIKE '%api%' THEN 'API'
      WHEN LOWER(description) LIKE '%database%' OR LOWER(description) LIKE '%db%' THEN 'Database'
      WHEN LOWER(description) LIKE '%login%' OR LOWER(description) LIKE '%auth%' THEN 'Authentication'
      WHEN LOWER(description) LIKE '%monitor%' THEN 'Monitoring'
      WHEN LOWER(description) LIKE '%backup%' THEN 'Backup'
      WHEN LOWER(description) LIKE '%cloud%' THEN 'Cloud Infrastructure'
      WHEN LOWER(description) LIKE '%production%' THEN 'Production'
      ELSE 'Other'
    END
  ORDER BY ds, system_type
),
max_date AS (
  SELECT MAX(ds) AS last_date FROM daily_system_issues
),
horizon_date AS (
  SELECT DATE_ADD(last_date, 7) AS horizon FROM max_date
)
SELECT 
  'System Issues Forecast' as forecast_type,
  'Next 7 Days' as forecast_period,
  system_type,
  *
FROM ai_forecast(
  TABLE(daily_system_issues),
  horizon => (SELECT horizon FROM horizon_date),
  time_col => 'ds',
  value_col => 'system_issue_count',
  group_col => 'system_type'
);
