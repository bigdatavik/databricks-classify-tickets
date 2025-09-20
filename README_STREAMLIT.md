# 🎫 AI Ticket Classification Dashboard

A Streamlit dashboard that transforms AI analysis into actionable business insights using Databricks Unity Catalog data.

## 🚀 Features

- **📊 Interactive Dashboards** - Visualize AI analysis results with charts and metrics
- **🎯 Business Intelligence** - Priority distribution, system health, and resource allocation
- **📈 Real-time Data** - Connect directly to Unity Catalog tables
- **🔧 Flexible Deployment** - Run on Databricks or locally

## 📋 Prerequisites

- Databricks workspace with Unity Catalog access
- SQL Warehouse ID: `148ccb90800933a1`
- Required privileges:
  - `SELECT` on Unity Catalog tables
  - `CAN USE` on SQL warehouse

## 🛠️ Installation

### For Databricks Deployment

1. **Deploy the app** to your Databricks workspace
2. **Configure permissions** for the app's service principal
3. **Access the dashboard** through Databricks Apps

### For Local Development

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set environment variables:**
   ```bash
   export DATABRICKS_WAREHOUSE_ID='148ccb90800933a1'
   ```

3. **Run locally:**
   ```bash
   python run_local.py
   ```
   
   Or manually:
   ```bash
   streamlit run app.py
   ```

## 📊 Data Sources

The dashboard connects to these Unity Catalog tables:

- `quickstart_catalog_vkm_external.classify_tickets.ai_showcase_results`
- `quickstart_catalog_vkm_external.classify_tickets.dashboard_priority_distribution`
- `quickstart_catalog_vkm_external.classify_tickets.dashboard_system_health`
- `quickstart_catalog_vkm_external.classify_tickets.dashboard_resource_allocation`

## 🎯 Dashboard Sections

### 1. AI Analysis Results
- Total tickets and urgent ticket counts
- Priority distribution charts
- Detailed analysis table

### 2. Priority Distribution
- Distribution by count and percentage
- Color-coded priority breakdown

### 3. System Health
- Health status distribution
- Urgent tickets by system
- System health details

### 4. Resource Allocation
- Priority score distribution
- Resource urgency breakdown
- Top priority tickets

## 🔧 Configuration

### Environment Variables

- `DATABRICKS_WAREHOUSE_ID` - SQL Warehouse ID (default: 148ccb90800933a1)
- `STREAMLIT_GATHER_USAGE_STATS` - Disable usage tracking (default: false)

### app.yaml

The `app.yaml` file configures the Databricks app runtime:

```yaml
command: ['streamlit', 'run', 'app.py', '--server.port=8501', '--server.address=0.0.0.0']
env:
  - name: 'DATABRICKS_WAREHOUSE_ID'
    value: '148ccb90800933a1'
  - name: 'STREAMLIT_GATHER_USAGE_STATS'
    value: 'false'
```

## 🚀 Usage

1. **Select a data source** from the sidebar
2. **View interactive charts** and metrics
3. **Analyze business insights** for decision making
4. **Export data** if needed

## 🔒 Security

- Uses Databricks SQL Connector for secure authentication
- Cached connections for performance
- Service principal authentication for Databricks deployment

## 📚 References

- [Databricks Streamlit Tutorial](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-apps/tutorial-streamlit)
- [Databricks App Runtime Configuration](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-apps/app-runtime)
