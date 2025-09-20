# 🎫 AI Ticket Classification Dashboard

A stunning Streamlit dashboard that transforms AI analysis into actionable business insights using Databricks Unity Catalog data. Features beautiful visualizations, interactive charts, and real-time analytics.

## ✨ WOW Features

### 🎨 **Visual Excellence**
- **Gradient Headers** - Beautiful animated text effects
- **Interactive Charts** - Plotly visualizations (pie, bar, scatter, gauge, donut)
- **Animated Cards** - Pulsing metric cards with professional shadows
- **Smooth Animations** - Fade-in effects and loading animations
- **Color-coded Alerts** - Success, warning, and error indicators

### 📊 **Interactive Dashboards**
- **Real-time Metrics** - Animated KPI cards with business insights
- **Priority Distribution** - Interactive pie and donut charts
- **System Health** - Gauge charts and health indicators
- **Resource Allocation** - Scatter plots and priority analysis
- **Business Intelligence** - Comprehensive data visualization

### 🚀 **User Experience**
- **Progress Bars** - Animated loading with status updates
- **Refresh Button** - Easy data reload functionality
- **Enhanced Sidebar** - Professional configuration interface
- **Responsive Design** - Works on all screen sizes
- **Professional Styling** - Modern UI with hover effects

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

2. **Configure Databricks profile:**
   ```bash
   databricks configure --profile DEFAULT
   ```

3. **Run locally:**
   ```bash
   python run_local.py
   ```
   
   Or manually:
   ```bash
   export DATABRICKS_WAREHOUSE_ID='148ccb90800933a1'
   streamlit run app.py
   ```

## 📊 Data Sources

The dashboard connects to these Unity Catalog tables:

- `quickstart_catalog_vkm_external.classify_tickets.ai_showcase_results`
- `quickstart_catalog_vkm_external.classify_tickets.dashboard_priority_distribution`
- `quickstart_catalog_vkm_external.classify_tickets.dashboard_system_health`
- `quickstart_catalog_vkm_external.classify_tickets.dashboard_resource_allocation`

## 🎯 Dashboard Sections

### 1. 🤖 AI Analysis Results
- **Animated Metrics**: Total tickets, urgent counts, high risk, systems affected
- **Interactive Charts**: Priority distribution pie and bar charts
- **Real-time Data**: Live updates from Unity Catalog
- **Detailed Analysis**: Comprehensive data table with enhanced styling

### 2. 📈 Priority Distribution
- **Donut Charts**: Interactive priority distribution visualization
- **Horizontal Bars**: Percentage-based priority breakdown
- **Color Coding**: Visual priority level indicators
- **Responsive Design**: Adapts to different screen sizes

### 3. 🏥 System Health
- **Gauge Charts**: Real-time system health indicators
- **Health Status**: Color-coded system status distribution
- **Urgent Alerts**: Visual urgent ticket identification
- **Health Metrics**: Comprehensive system health details

### 4. 🎯 Resource Allocation
- **Histograms**: Priority score distribution analysis
- **Scatter Plots**: Priority vs urgency correlation
- **Urgency Breakdown**: Interactive urgency level charts
- **Top Priority**: Highlighted high-priority tickets

## 🔧 Configuration

### Environment Variables

- `DATABRICKS_WAREHOUSE_ID` - SQL Warehouse ID (default: 148ccb90800933a1)
- `DATABRICKS_CONFIG_PROFILE` - Databricks profile (default: DEFAULT)
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

### Quick Start
1. **Launch the dashboard**: `python run_local.py`
2. **Select a data source** from the sidebar dropdown
3. **View interactive charts** and animated metrics
4. **Analyze business insights** with real-time data
5. **Refresh data** using the refresh button

### Advanced Features
- **Interactive Exploration**: Click and hover on charts for details
- **Real-time Updates**: Data refreshes automatically
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Export Capabilities**: Download data and charts
- **Custom Filtering**: Filter data by priority, system, or urgency

## 🛠️ Technical Features

### Frontend Technologies
- **Streamlit**: Modern web app framework
- **Plotly**: Interactive data visualizations
- **Custom CSS**: Professional styling and animations
- **Responsive Design**: Mobile-first approach

### Backend Integration
- **Databricks SQL Connector**: Secure data connectivity
- **Unity Catalog**: Enterprise data governance
- **Cached Connections**: Optimized performance
- **Error Handling**: Robust error management

### Performance Optimizations
- **Connection Caching**: Reduced connection overhead
- **Lazy Loading**: Efficient data loading
- **Progress Indicators**: User feedback during operations
- **Memory Management**: Optimized data processing

## 🔒 Security

- Uses Databricks SQL Connector for secure authentication
- Cached connections for performance
- Service principal authentication for Databricks deployment

## 📚 References

- [Databricks Streamlit Tutorial](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-apps/tutorial-streamlit)
- [Databricks App Runtime Configuration](https://learn.microsoft.com/en-us/azure/databricks/dev-tools/databricks-apps/app-runtime)
