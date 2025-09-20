# Databricks Ticket Classification - Configuration
# Unity Catalog and Default Databricks Configuration

import os

# Unity Catalog Configuration
UNITY_CATALOG = {
    "catalog_name": "quickstart_catalog_vkm_external",
    "schema_name": "classify_tickets",
    "volume_name": "classify_tickets_volume"
}

# Table Names with Unity Catalog (3-level namespace)
TABLES = {
    "raw_tickets": f"{UNITY_CATALOG['catalog_name']}.{UNITY_CATALOG['schema_name']}.raw_tickets",
    "tickets_with_actions": f"{UNITY_CATALOG['catalog_name']}.{UNITY_CATALOG['schema_name']}.tickets_with_actions",
    "action_items_detailed": f"{UNITY_CATALOG['catalog_name']}.{UNITY_CATALOG['schema_name']}.action_items_detailed",
    "tickets_ai_classified": f"{UNITY_CATALOG['catalog_name']}.{UNITY_CATALOG['schema_name']}.tickets_ai_classified",
    "action_items_ai_classified": f"{UNITY_CATALOG['catalog_name']}.{UNITY_CATALOG['schema_name']}.action_items_ai_classified",
    "tickets_classified_final": f"{UNITY_CATALOG['catalog_name']}.{UNITY_CATALOG['schema_name']}.tickets_classified_final",
    "action_items_classified_final": f"{UNITY_CATALOG['catalog_name']}.{UNITY_CATALOG['schema_name']}.action_items_classified_final",
    "ai_showcase_results": f"{UNITY_CATALOG['catalog_name']}.{UNITY_CATALOG['schema_name']}.ai_showcase_results",
    "dashboard_priority_distribution": f"{UNITY_CATALOG['catalog_name']}.{UNITY_CATALOG['schema_name']}.dashboard_priority_distribution",
    "dashboard_system_health": f"{UNITY_CATALOG['catalog_name']}.{UNITY_CATALOG['schema_name']}.dashboard_system_health",
    "dashboard_resource_allocation": f"{UNITY_CATALOG['catalog_name']}.{UNITY_CATALOG['schema_name']}.dashboard_resource_allocation"
}

# Databricks Configuration
DATABRICKS_CONFIG = {
    "profile": os.getenv("DATABRICKS_CONFIG_PROFILE", "DEFAULT"),
    "cluster_id": os.getenv("DATABRICKS_CLUSTER_ID", None),
    "warehouse_id": os.getenv("DATABRICKS_WAREHOUSE_ID", None)
}

# Pipeline Configuration
PIPELINE_CONFIG = {
    # Input/Output tables (Unity Catalog format)
    "input_table": TABLES["raw_tickets"],
    "output_table_tickets": TABLES["tickets_classified_final"], 
    "output_table_actions": TABLES["action_items_classified_final"],
    
    # Processing options
    "batch_size": 100,
    "enable_ai_summaries": True,
    "enable_next_steps": True,
    
    # Quality settings
    "min_action_length": 3,
    "max_action_items": 50,
    
    # Unity Catalog settings
    "use_unity_catalog": True,
    "catalog_name": UNITY_CATALOG["catalog_name"],
    "schema_name": UNITY_CATALOG["schema_name"]
}

# AI Model Configuration
AI_CONFIG = {
    "default_model": "databricks-meta-llama-3-1-70b-instruct",
    "classification_model": "databricks-meta-llama-3-1-70b-instruct",
    "generation_model": "databricks-meta-llama-3-1-70b-instruct"
}

# Classification Categories
CLASSIFICATION_CATEGORIES = {
    "priorities": [
        "P0 - Critical",
        "P1 - High", 
        "P2 - Medium",
        "P3 - Low",
        "P4 - Planning"
    ],
    
    "categories": [
        "Infrastructure Change",
        "Security Update",
        "Application Support",
        "Database Maintenance",
        "Network Configuration", 
        "Monitoring Setup",
        "Backup & Recovery",
        "Performance Optimization",
        "User Management",
        "Compliance & Audit",
        "Other"
    ],
    
    "technologies": [
        "Azure Cloud Platform",
        "AWS Cloud Platform", 
        "Google Cloud Platform",
        "Kubernetes",
        "Docker",
        "Azure SQL Database",
        "PostgreSQL",
        "MongoDB",
        "Redis",
        "Apache Kafka",
        "Apache Spark",
        "Databricks",
        "Power BI",
        "Tableau",
        "Jenkins",
        "Azure DevOps",
        "GitHub Actions",
        "Terraform",
        "Ansible",
        "Other"
    ],
    
    "risk_levels": [
        "Low Risk",
        "Medium Risk", 
        "High Risk",
        "Critical Risk"
    ],
    
    "effort_estimates": [
        "1-2 hours",
        "Half day (4 hours)",
        "Full day (8 hours)", 
        "2-3 days",
        "1 week",
        "2+ weeks"
    ],
    
    "action_types": [
        "Installation",
        "Configuration", 
        "Testing",
        "Documentation",
        "Monitoring",
        "Backup",
        "Security Review",
        "Performance Testing",
        "User Training",
        "Compliance Check",
        "Other"
    ],
    
    "action_complexity": [
        "Simple",
        "Moderate", 
        "Complex",
        "Very Complex"
    ]
}

def get_unity_catalog_table_name(table_key):
    """Get the full Unity Catalog table name for a given table key"""
    return TABLES.get(table_key, f"{UNITY_CATALOG['catalog_name']}.{UNITY_CATALOG['schema_name']}.{table_key}")

def get_sql_create_schema():
    """Get SQL command to create the Unity Catalog schema"""
    return f"""
    CREATE SCHEMA IF NOT EXISTS {UNITY_CATALOG['catalog_name']}.{UNITY_CATALOG['schema_name']}
    COMMENT 'Schema for Databricks ticket classification system using Unity Catalog'
    """

def get_sql_create_volume():
    """Get SQL command to create Unity Catalog volume for file storage"""
    return f"""
    CREATE VOLUME IF NOT EXISTS {UNITY_CATALOG['catalog_name']}.{UNITY_CATALOG['schema_name']}.{UNITY_CATALOG['volume_name']}
    COMMENT 'Volume for storing ticket classification files and artifacts'
    """