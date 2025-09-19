# 🚀 Databricks Workflow Deployment Guide

This guide explains how to deploy and run the three notebooks in sequence using Databricks Asset Bundles.

## 📋 Workflow Overview

The workflow runs three notebooks in sequence:

1. **01_sample_data_generation.ipynb** - Generates realistic ticket data
2. **02_action_extraction.ipynb** - Extracts action items using AI
3. **03_ai_classification.ipynb** - Performs AI-powered classification
4. **validation_summary.ipynb** - Validates results and provides summary

## 🔧 Configuration Files

### 1. Main Job Configuration
- **File**: `resources/databricks_classify_tickets.job.yml`
- **Purpose**: Primary workflow with basic sequential execution
- **Features**: Simple dependencies, timeouts, retry logic

### 2. Advanced Workflow Configuration
- **File**: `resources/notebook_workflow.yml`
- **Purpose**: Enhanced workflow with better error handling
- **Features**: Email notifications, detailed logging, validation step

## 🚀 Deployment Steps

### Step 1: Deploy the Bundle
```bash
# Deploy to development environment
databricks bundle deploy

# Deploy to production environment
databricks bundle deploy --target prod
```

### Step 2: Run the Workflow
```bash
# Run the main job
databricks jobs run-now --job-id <job_id>

# Or run the advanced workflow
databricks jobs run-now --job-id <advanced_job_id>
```

### Step 3: Monitor Execution
- Check the Databricks Jobs UI for execution status
- View logs for each task in the workflow
- Monitor email notifications for failures/success

## 📊 Workflow Dependencies

```
01_data_generation
    ↓
02_action_extraction
    ↓
03_ai_classification
    ↓
04_validation (optional)
```

## ⚙️ Configuration Options

### Timeouts
- **Data Generation**: 30 minutes
- **Action Extraction**: 60 minutes (AI processing)
- **AI Classification**: 30 minutes
- **Validation**: 15 minutes

### Retry Logic
- **Max Retries**: 2 per task
- **Retry on Timeout**: Enabled
- **Exponential Backoff**: Automatic

### Notifications
- **On Failure**: Email alerts
- **On Success**: Optional email confirmation
- **Logging**: Detailed task logs

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
