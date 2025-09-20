# 🚀 AI Ticket Classification Dashboard - Deployment Guide

This comprehensive guide covers deploying the complete AI Ticket Classification system, including the Databricks workflow and the stunning Streamlit dashboard.

## 📋 Project Overview

The project consists of two main components:

### 1. 🤖 Databricks AI Workflow
- **01_sample_data_generation.ipynb** - Generates realistic ticket data
- **02_ai_showcase.ipynb** - Demonstrates all three AI functions (ai_classify, ai_extract, ai_gen)
- **03_business_insights.ipynb** - Generates business insights and dashboard data

### 2. 🎨 Streamlit Dashboard
- **Interactive Visualizations** - Plotly charts and animated metrics
- **Real-time Data** - Live connection to Unity Catalog
- **Business Intelligence** - Priority analysis, system health, resource allocation
- **Beautiful UI** - Modern design with animations and professional styling

## 🔧 Configuration Files

### 1. Databricks Job Configuration
- **File**: `resources/databricks_classify_tickets.job.yml`
- **Purpose**: AI workflow with sequential execution
- **Features**: Job clusters, timeouts, retry logic, email notifications

### 2. Streamlit App Configuration
- **File**: `app.yaml`
- **Purpose**: Streamlit app runtime configuration
- **Features**: Environment variables, port configuration, command setup

### 3. Asset Bundle Configuration
- **File**: `databricks.yml`
- **Purpose**: Main bundle configuration
- **Features**: Target environments, resource definitions

## 🚀 Deployment Steps

### Step 1: Prerequisites
```bash
# Install Databricks CLI
pip install databricks-cli

# Configure authentication
databricks configure --profile DEFAULT

# Install project dependencies
pip install -r requirements.txt
```

### Step 2: Deploy the Databricks Workflow
```bash
# Deploy to development environment
databricks bundle deploy --target dev

# Deploy to production environment
databricks bundle deploy --target prod
```

### Step 3: Run the AI Workflow
```bash
# Run the complete workflow
databricks bundle run

# Or run individual jobs
databricks jobs run-now --job-id <job_id>
```

### Step 4: Deploy the Streamlit Dashboard
```bash
# Deploy the Streamlit app to Databricks
databricks bundle deploy --target dev

# Or run locally for development
python run_local.py
```

### Step 5: Access the Dashboard
- **Databricks**: Access through Databricks Apps
- **Local**: Open http://localhost:8501
- **Production**: Use your Databricks workspace URL

## 📊 Workflow Dependencies

```
01_data_generation
    ↓
02_ai_showcase (ai_classify, ai_extract, ai_gen)
    ↓
03_business_insights (dashboard data generation)
    ↓
Streamlit Dashboard (real-time visualization)
```

## ⚙️ Configuration Options

### Databricks Job Timeouts
- **Data Generation**: 30 minutes
- **AI Showcase**: 60 minutes (AI processing)
- **Business Insights**: 30 minutes
- **Total Workflow**: 2 hours

### Streamlit Dashboard Configuration
- **Port**: 8501 (default)
- **Host**: 0.0.0.0 (for Databricks deployment)
- **Warehouse ID**: 148ccb90800933a1
- **Profile**: DEFAULT

### Retry Logic
- **Max Retries**: 2 per task
- **Retry on Timeout**: Enabled
- **Exponential Backoff**: Automatic

### Notifications
- **On Failure**: Email alerts to vik.malhotra@databricks.com
- **On Success**: Email confirmation
- **Logging**: Detailed task logs

## 🎨 Streamlit Dashboard Features

### Visual Components
- **Interactive Charts**: Plotly visualizations
- **Animated Metrics**: Real-time KPI cards
- **Gradient Headers**: Beautiful text effects
- **Color-coded Alerts**: Status indicators
- **Responsive Design**: Mobile-friendly interface

### Data Sources
- **Unity Catalog Tables**: Real-time data access
- **SQL Warehouse**: Live data connectivity
- **Cached Connections**: Optimized performance
- **Error Handling**: Robust data loading

### Business Intelligence
- **Priority Analysis**: Interactive distribution charts
- **System Health**: Gauge charts and health indicators
- **Resource Allocation**: Scatter plots and recommendations
- **Executive Summary**: High-level insights

## 🔍 Monitoring and Troubleshooting

### Common Issues
1. **Timeout Errors**: Increase timeout values in job configuration
2. **Memory Issues**: Adjust cluster configuration
3. **AI Function Limits**: Check Databricks AI Functions quotas
4. **Table Access**: Verify Unity Catalog permissions

### Debugging Steps
1. Check individual task logs in Databricks Jobs UI
2. Verify table existence and permissions
3. Test notebooks individually before running workflow
4. Check cluster resources and configuration

## 📈 Performance Optimization

### Recommendations
1. **Use Serverless Compute**: For cost efficiency
2. **Enable Auto-scaling**: For variable workloads
3. **Cache DataFrames**: For repeated operations
4. **Batch AI Operations**: For better performance

### Resource Requirements
- **Minimum**: 2-4 cores, 8GB RAM
- **Recommended**: 4-8 cores, 16-32GB RAM
- **For Large Datasets**: 8+ cores, 32+ GB RAM

## 🔐 Security Considerations

### Unity Catalog
- Ensure proper table permissions
- Use service principals for automated runs
- Enable audit logging

### Data Privacy
- Review data classification
- Implement data masking if needed
- Follow compliance requirements

## 📝 Customization

### Adding Parameters
```yaml
base_parameters:
  num_tickets: "50"
  data_quality: "realistic"
  processing_mode: "batch"
```

### Modifying Schedule
```yaml
trigger:
  periodic:
    interval: 1
    unit: DAYS
    # Or use cron expressions
    quartz_cron_expression: "0 0 9 * * ?"
```

### Adding Dependencies
```yaml
depends_on:
  - task_key: "previous_task"
  - task_key: "another_task"
```

## 🎯 Next Steps

1. **Test the Workflow**: Run in development first
2. **Monitor Performance**: Track execution times and costs
3. **Optimize**: Adjust timeouts and resources as needed
4. **Scale**: Increase data volume gradually
5. **Automate**: Set up proper scheduling and monitoring

## 📞 Support

For issues or questions:
- Check Databricks documentation
- Review job logs and error messages
- Contact your Databricks administrator
- Use Databricks support channels
