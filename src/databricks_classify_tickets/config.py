# Databricks Ticket Classification - Configuration
# Unity Catalog Configuration

# Unity Catalog Configuration
UNITY_CATALOG = {
    "catalog_name": "quickstart_catalog_vkm_external",
    "schema_name": "classify_tickets"
}

# Table Names with Unity Catalog (3-level namespace)
# Only includes tables that are actually used in the project
TABLES = {
    "raw_tickets": f"{UNITY_CATALOG['catalog_name']}.{UNITY_CATALOG['schema_name']}.raw_tickets",
    "ai_showcase_results": f"{UNITY_CATALOG['catalog_name']}.{UNITY_CATALOG['schema_name']}.ai_showcase_results",
    "dashboard_priority_distribution": f"{UNITY_CATALOG['catalog_name']}.{UNITY_CATALOG['schema_name']}.dashboard_priority_distribution",
    "dashboard_system_health": f"{UNITY_CATALOG['catalog_name']}.{UNITY_CATALOG['schema_name']}.dashboard_system_health",
    "dashboard_resource_allocation": f"{UNITY_CATALOG['catalog_name']}.{UNITY_CATALOG['schema_name']}.dashboard_resource_allocation"
}