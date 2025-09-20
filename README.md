# 🎫 AI Ticket Classification Dashboard

A comprehensive Databricks project that demonstrates the power of AI functions (`ai_classify`, `ai_extract`, `ai_gen`) for intelligent ticket classification and business insights generation. Features a stunning Streamlit dashboard with interactive visualizations and real-time data analysis.

## ✨ Features

### 🤖 AI-Powered Analysis
- **AI Classification**: Automatically classify ticket priorities using `ai_classify`
- **AI Extraction**: Extract structured data (action items, requirements, urgency) using `ai_extract`
- **AI Generation**: Generate comprehensive analysis and recommendations using `ai_gen`

### 📊 Interactive Dashboard
- **Beautiful UI**: Modern Streamlit interface with gradient headers and animations
- **Interactive Charts**: Plotly visualizations (pie, bar, scatter, gauge, donut charts)
- **Real-time Metrics**: Animated metric cards with business KPIs
- **System Health**: Gauge charts and health indicators
- **Resource Allocation**: Scatter plots and priority analysis

### 🏗️ Databricks Integration
- **Unity Catalog**: Seamless data storage and retrieval
- **Job Workflows**: Automated data processing pipeline
- **SQL Warehouse**: Real-time data connectivity
- **Asset Bundles**: Production-ready deployment configuration

## 🚀 Quick Start

### Prerequisites
- Databricks workspace with AI functions enabled
- Python 3.8+ with pip
- Databricks CLI configured

### Local Development
1. **Clone and setup:**
   ```bash
   git clone <repository-url>
   cd databricks_classify_tickets
   pip install -r requirements.txt
   ```

2. **Configure Databricks:**
   ```bash
   databricks configure --profile DEFAULT
   ```

3. **Run the Streamlit dashboard:**
   ```bash
   python run_local.py
   ```
   Open your browser to: http://localhost:8501

### Databricks Deployment
1. **Deploy the job:**
   ```bash
   databricks bundle deploy --target dev
   ```

2. **Run the workflow:**
   ```bash
   databricks bundle run
   ```

3. **Deploy the Streamlit app:**
   ```bash
   databricks bundle deploy --target dev
   ```

## 📁 Project Structure

```
databricks_classify_tickets/
├── src/databricks_classify_tickets/
│   ├── 01_sample_data_generation.ipynb    # Generate realistic ticket data
│   ├── 02_ai_showcase.ipynb               # AI functions demonstration
│   ├── 03_business_insights.ipynb         # Business analysis and KPIs
│   └── config.py                          # Unity Catalog configuration
├── resources/
│   └── databricks_classify_tickets.job.yml # Job workflow definition
├── app.py                                 # Streamlit dashboard
├── app.yaml                              # Streamlit app configuration
├── run_local.py                          # Local development script
├── requirements.txt                      # Python dependencies
└── databricks.yml                        # Asset bundle configuration
```

## 🔧 Configuration

### Environment Variables
- `DATABRICKS_WAREHOUSE_ID`: SQL Warehouse ID (default: 148ccb90800933a1)
- `DATABRICKS_CONFIG_PROFILE`: Databricks profile (default: DEFAULT)
- `STREAMLIT_GATHER_USAGE_STATS`: Disable usage tracking (default: false)

### Unity Catalog Tables
- `ai_showcase_results`: Main AI analysis results
- `dashboard_priority_distribution`: Priority analysis data
- `dashboard_system_health`: System health metrics
- `dashboard_resource_allocation`: Resource allocation recommendations

## 📊 Dashboard Features

### 🤖 AI Analysis Results
- Interactive priority distribution charts
- Real-time ticket metrics
- Action items extraction
- Urgency level analysis

### 📈 Business Insights
- Priority distribution analysis
- System health monitoring
- Resource allocation recommendations
- Executive summary generation

### 🎨 Visual Enhancements
- Gradient headers and animated cards
- Interactive Plotly visualizations
- Color-coded alerts and status indicators
- Smooth loading animations
- Professional styling

## 🛠️ Development

### Running Tests
```bash
# Run the complete workflow
databricks bundle run

# Test individual notebooks
# Open in Databricks workspace and run cells
```

### Customizing the Dashboard
- Modify `app.py` for UI changes
- Update `config.py` for table configurations
- Add new visualizations in display functions

## 📚 Documentation

- [Streamlit Dashboard Guide](README_STREAMLIT.md)
- [Deployment Guide](DEPLOYMENT_GUIDE.md)
- [Databricks Asset Bundles](https://docs.databricks.com/dev-tools/bundles/index.html)
- [Streamlit Documentation](https://docs.streamlit.io/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## 🙏 Acknowledgments

- Databricks AI Functions team
- Streamlit community
- Plotly for interactive visualizations
