#!/usr/bin/env python3
"""
Local development script for the AI Ticket Classification Dashboard
Run this script to start the Streamlit app locally with proper environment variables
Uses DEFAULT Databricks profile for authentication
"""

import os
import subprocess
import sys

def main():
    # Set environment variables for local development
    os.environ['DATABRICKS_WAREHOUSE_ID'] = '148ccb90800933a1'
    os.environ['STREAMLIT_GATHER_USAGE_STATS'] = 'false'
    os.environ['DATABRICKS_CONFIG_PROFILE'] = 'DEFAULT'
    os.environ['UNITY_CATALOG_NAME'] = 'quickstart_catalog_vkm_external'
    os.environ['UNITY_SCHEMA_NAME'] = 'classify_tickets'
    
    print("🚀 Starting AI Ticket Classification Dashboard locally...")
    print(f"📊 Warehouse ID: {os.environ['DATABRICKS_WAREHOUSE_ID']}")
    print(f"🗄️  Catalog: {os.environ['UNITY_CATALOG_NAME']}")
    print(f"📁 Schema: {os.environ['UNITY_SCHEMA_NAME']}")
    print(f"🔐 Using Databricks profile: {os.environ['DATABRICKS_CONFIG_PROFILE']}")
    print("🌐 Open your browser to: http://localhost:8501")
    print("=" * 60)
    
    # Run streamlit
    try:
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run', 'app.py',
            '--server.port=8501',
            '--server.address=localhost'
        ])
    except KeyboardInterrupt:
        print("\n👋 Dashboard stopped by user")
    except Exception as e:
        print(f"❌ Error starting dashboard: {e}")

if __name__ == "__main__":
    main()
