import streamlit as st
import pandas as pd
from databricks import sql
from databricks.sdk.core import Config
import os
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import time
import numpy as np

# Page configuration
st.set_page_config(
    page_title="🎫 AI Ticket Classification Dashboard",
    page_icon="🎫",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://docs.streamlit.io',
        'Report a bug': "https://github.com/streamlit/streamlit/issues",
        'About': "# AI Ticket Classification Dashboard\n*Transform AI analysis into actionable business insights*"
    }
)

# Custom CSS for wow factor
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
        margin: 0.5rem 0;
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
    }
    
    .metric-label {
        font-size: 1rem;
        opacity: 0.9;
        margin: 0;
    }
    
    .section-header {
        font-size: 2rem;
        font-weight: 600;
        color: #2c3e50;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #667eea;
    }
    
    .success-box {
        background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
        box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
    }
    
    .warning-box {
        background: linear-gradient(135deg, #ff9800 0%, #f57c00 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
        box-shadow: 0 4px 15px rgba(255, 152, 0, 0.3);
    }
    
    .error-box {
        background: linear-gradient(135deg, #f44336 0%, #d32f2f 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        text-align: center;
        box-shadow: 0 4px 15px rgba(244, 67, 54, 0.3);
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    .stSelectbox > div > div {
        background-color: #f8f9fa;
        border-radius: 10px;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    .dataframe {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .loading-spinner {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 200px;
    }
    
    .pulse {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .fade-in {
        animation: fadeIn 1s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

# Initialize Databricks configuration
cfg = Config()

# Get catalog and schema from environment variables
CATALOG_NAME = os.getenv("UNITY_CATALOG_NAME", "quickstart_catalog_vkm_external")
SCHEMA_NAME = os.getenv("UNITY_SCHEMA_NAME", "classify_tickets")

@st.cache_resource
def get_connection(http_path):
    """Create a cached SQL connection to Databricks"""
    return sql.connect(
        server_hostname=cfg.host,
        http_path=http_path,
        credentials_provider=lambda: cfg.authenticate,
    )

def read_table(table_name: str, conn) -> pd.DataFrame:
    """Read data from a Unity Catalog table"""
    with conn.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {table_name}")
        return cursor.fetchall_arrow().to_pandas()

def get_warehouse_id():
    """Get warehouse ID from environment variable or user input"""
    return os.getenv('DATABRICKS_WAREHOUSE_ID', '')

# Main app
def main():
    # Animated header
    st.markdown('<h1 class="main-header fade-in">🎫 AI Ticket Classification Dashboard</h1>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666; margin-bottom: 2rem;" class="fade-in">✨ Transform AI analysis into actionable business insights ✨</p>', unsafe_allow_html=True)
    
    # Sidebar for configuration
    with st.sidebar:
        st.markdown('<h2 style="color: white; text-align: center;">⚙️ Configuration</h2>', unsafe_allow_html=True)
        
        # Get warehouse ID
        warehouse_id = get_warehouse_id()
        if warehouse_id:
            st.markdown(f'<div class="success-box">✅ Warehouse ID: {warehouse_id}</div>', unsafe_allow_html=True)
            http_path = f"/sql/1.0/warehouses/{warehouse_id}"
        else:
            st.markdown('<div class="warning-box">⚠️ No warehouse ID found in environment</div>', unsafe_allow_html=True)
            http_path = st.text_input(
                "Enter Databricks HTTP Path:",
                placeholder="/sql/1.0/warehouses/xxxxxx",
                help="Set DATABRICKS_WAREHOUSE_ID environment variable for automatic detection"
            )
        
        # Table selection
        st.markdown('<h3 style="color: white;">📊 Data Sources</h3>', unsafe_allow_html=True)
        table_options = [
            f"{CATALOG_NAME}.{SCHEMA_NAME}.ai_showcase_results",
            f"{CATALOG_NAME}.{SCHEMA_NAME}.dashboard_priority_distribution",
            f"{CATALOG_NAME}.{SCHEMA_NAME}.dashboard_system_health",
            f"{CATALOG_NAME}.{SCHEMA_NAME}.dashboard_resource_allocation"
        ]
        
        selected_table = st.selectbox(
            "Select Table:",
            table_options,
            help="Choose which dashboard data to display"
        )
        
        # Add refresh button
        if st.button("🔄 Refresh Data", use_container_width=True):
            st.rerun()
    
    # Main content area
    if http_path and selected_table:
        try:
            # Animated loading
            with st.spinner("🔄 Connecting to Databricks..."):
                time.sleep(1)  # Add a small delay for effect
                conn = get_connection(http_path)
            
            # Load data with progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            status_text.text("📊 Loading data...")
            progress_bar.progress(25)
            time.sleep(0.5)
            
            df = read_table(selected_table, conn)
            progress_bar.progress(75)
            time.sleep(0.5)
            
            progress_bar.progress(100)
            status_text.text("✅ Data loaded successfully!")
            time.sleep(0.5)
            
            progress_bar.empty()
            status_text.empty()
            
            if df.empty:
                st.markdown('<div class="warning-box">⚠️ No data found in the selected table</div>', unsafe_allow_html=True)
                return
            
            # Display data based on table type with animations
            if "ai_showcase_results" in selected_table:
                display_ai_showcase_results(df)
            elif "priority_distribution" in selected_table:
                display_priority_distribution(df)
            elif "system_health" in selected_table:
                display_system_health(df)
            elif "resource_allocation" in selected_table:
                display_resource_allocation(df)
            else:
                display_generic_table(df)
                
        except Exception as e:
            st.markdown(f'<div class="error-box">❌ Error connecting to Databricks: {str(e)}</div>', unsafe_allow_html=True)
            st.markdown('<div class="warning-box">💡 Make sure you have the correct warehouse ID and proper permissions</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="warning-box">⚠️ Please provide both the warehouse path and select a table to load data.</div>', unsafe_allow_html=True)

def display_ai_showcase_results(df):
    """Display AI showcase results with business insights"""
    st.markdown('<h2 class="section-header fade-in">🤖 AI Analysis Results</h2>', unsafe_allow_html=True)
    
    # Animated metrics with custom styling
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f'''
        <div class="metric-card pulse">
            <div class="metric-value">{len(df)}</div>
            <div class="metric-label">Total Tickets</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        urgent_count = len(df[df['ai_priority_classification'] == 'Urgent Priority'])
        st.markdown(f'''
        <div class="metric-card pulse">
            <div class="metric-value">{urgent_count}</div>
            <div class="metric-label">Urgent Tickets</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col3:
        high_risk = len(df[df['urgency_level'].str.contains('urgent|asap|high', case=False, na=False)])
        st.markdown(f'''
        <div class="metric-card pulse">
            <div class="metric-value">{high_risk}</div>
            <div class="metric-label">High Risk</div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col4:
        unique_systems = df['affected_systems'].nunique()
        st.markdown(f'''
        <div class="metric-card pulse">
            <div class="metric-value">{unique_systems}</div>
            <div class="metric-label">Systems Affected</div>
        </div>
        ''', unsafe_allow_html=True)
    
    # Interactive priority distribution with Plotly
    st.markdown('<h3 class="section-header fade-in">📊 Priority Distribution</h3>', unsafe_allow_html=True)
    priority_counts = df['ai_priority_classification'].value_counts()
    
    # Create beautiful pie chart
    fig_pie = px.pie(
        values=priority_counts.values, 
        names=priority_counts.index,
        title="Ticket Priority Distribution",
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    fig_pie.update_layout(
        title_font_size=20,
        font=dict(size=14),
        showlegend=True,
        height=400
    )
    
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig_pie, use_container_width=True)
    
    # Create bar chart
    with col2:
        fig_bar = px.bar(
            x=priority_counts.index, 
            y=priority_counts.values,
            title="Priority Counts",
            color=priority_counts.values,
            color_continuous_scale="Viridis"
        )
        fig_bar.update_layout(
            title_font_size=20,
            font=dict(size=14),
            height=400,
            xaxis_title="Priority Level",
            yaxis_title="Count"
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    
    # Detailed table with enhanced styling
    st.markdown('<h3 class="section-header fade-in">📋 Detailed Analysis</h3>', unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True, height=400)

def display_priority_distribution(df):
    """Display priority distribution with charts"""
    st.markdown('<h2 class="section-header fade-in">📈 Priority Distribution Analysis</h2>', unsafe_allow_html=True)
    
    # Create stunning visualizations
    col1, col2 = st.columns(2)
    
    with col1:
        # Interactive donut chart
        fig_donut = px.pie(
            df, 
            values='ticket_count', 
            names='priority_level',
            title="Distribution by Count",
            hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        fig_donut.update_traces(textposition='inside', textinfo='percent+label')
        fig_donut.update_layout(
            title_font_size=18,
            font=dict(size=12),
            height=400
        )
        st.plotly_chart(fig_donut, use_container_width=True)
    
    with col2:
        # Horizontal bar chart
        fig_hbar = px.bar(
            df, 
            x='percentage', 
            y='priority_level',
            orientation='h',
            title="Distribution by Percentage",
            color='percentage',
            color_continuous_scale="Blues"
        )
        fig_hbar.update_layout(
            title_font_size=18,
            font=dict(size=12),
            height=400,
            xaxis_title="Percentage (%)",
            yaxis_title="Priority Level"
        )
        st.plotly_chart(fig_hbar, use_container_width=True)
    
    # Color-coded table with enhanced styling
    st.markdown('<h3 class="section-header fade-in">📊 Priority Breakdown</h3>', unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True, height=300)

def display_system_health(df):
    """Display system health analysis"""
    st.markdown('<h2 class="section-header fade-in">🏥 System Health Analysis</h2>', unsafe_allow_html=True)
    
    # Health status distribution
    health_counts = df['health_status'].value_counts()
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Health status gauge chart
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = len(df[df['health_status'] == 'Good']),
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Systems in Good Health"},
            delta = {'reference': len(df)},
            gauge = {
                'axis': {'range': [None, len(df)]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, len(df)*0.5], 'color': "lightgray"},
                    {'range': [len(df)*0.5, len(df)*0.8], 'color': "yellow"},
                    {'range': [len(df)*0.8, len(df)], 'color': "green"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': len(df)*0.9
                }
            }
        ))
        fig_gauge.update_layout(height=400)
        st.plotly_chart(fig_gauge, use_container_width=True)
    
    with col2:
        # Health status pie chart
        fig_health = px.pie(
            values=health_counts.values, 
            names=health_counts.index,
            title="Health Status Distribution",
            color_discrete_map={
                'Good': '#4CAF50',
                'Fair': '#FF9800', 
                'Poor': '#FF5722',
                'Critical': '#F44336'
            }
        )
        fig_health.update_traces(textposition='inside', textinfo='percent+label')
        fig_health.update_layout(
            title_font_size=18,
            font=dict(size=12),
            height=400
        )
        st.plotly_chart(fig_health, use_container_width=True)
    
    # Urgent tickets by system
    st.markdown('<h3 class="section-header fade-in">🚨 Urgent Tickets by System</h3>', unsafe_allow_html=True)
    urgent_systems = df[df['urgent_tickets'] > 0]
    if not urgent_systems.empty:
        fig_urgent = px.bar(
            urgent_systems, 
            x='urgent_tickets', 
            y='system_name',
            orientation='h',
            title="Urgent Tickets by System",
            color='urgent_tickets',
            color_continuous_scale="Reds"
        )
        fig_urgent.update_layout(
            title_font_size=18,
            font=dict(size=12),
            height=400,
            xaxis_title="Urgent Tickets",
            yaxis_title="System Name"
        )
        st.plotly_chart(fig_urgent, use_container_width=True)
    else:
        st.markdown('<div class="success-box">✅ No urgent tickets found - All systems healthy!</div>', unsafe_allow_html=True)
    
    # System health table
    st.markdown('<h3 class="section-header fade-in">📊 System Health Details</h3>', unsafe_allow_html=True)
    st.dataframe(df, use_container_width=True, height=400)

def display_resource_allocation(df):
    """Display resource allocation recommendations"""
    st.markdown('<h2 class="section-header fade-in">🎯 Resource Allocation Recommendations</h2>', unsafe_allow_html=True)
    
    # Priority score distribution
    st.markdown('<h3 class="section-header fade-in">📊 Priority Score Distribution</h3>', unsafe_allow_html=True)
    priority_scores = df['priority_score'].value_counts().sort_index()
    
    # Create histogram
    fig_hist = px.histogram(
        df, 
        x='priority_score',
        title="Priority Score Distribution",
        nbins=10,
        color_discrete_sequence=['#667eea']
    )
    fig_hist.update_layout(
        title_font_size=18,
        font=dict(size=12),
        height=400,
        xaxis_title="Priority Score",
        yaxis_title="Count"
    )
    st.plotly_chart(fig_hist, use_container_width=True)
    
    # Resource urgency breakdown
    st.markdown('<h3 class="section-header fade-in">⚡ Resource Urgency Breakdown</h3>', unsafe_allow_html=True)
    urgency_counts = df['resource_urgency'].value_counts()
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Urgency pie chart
        fig_urgency = px.pie(
            values=urgency_counts.values, 
            names=urgency_counts.index,
            title="Resource Urgency Distribution",
            color_discrete_map={
                'Immediate': '#F44336',
                'High': '#FF9800',
                'Medium': '#FFC107',
                'Low': '#4CAF50'
            }
        )
        fig_urgency.update_traces(textposition='inside', textinfo='percent+label')
        fig_urgency.update_layout(
            title_font_size=18,
            font=dict(size=12),
            height=400
        )
        st.plotly_chart(fig_urgency, use_container_width=True)
    
    with col2:
        # Urgency bar chart
        fig_urgency_bar = px.bar(
            x=urgency_counts.index, 
            y=urgency_counts.values,
            title="Urgency Counts",
            color=urgency_counts.values,
            color_continuous_scale="RdYlGn_r"
        )
        fig_urgency_bar.update_layout(
            title_font_size=18,
            font=dict(size=12),
            height=400,
            xaxis_title="Urgency Level",
            yaxis_title="Count"
        )
        st.plotly_chart(fig_urgency_bar, use_container_width=True)
    
    # Top priority tickets with enhanced styling
    st.markdown('<h3 class="section-header fade-in">🚨 Top Priority Tickets</h3>', unsafe_allow_html=True)
    top_tickets = df.nlargest(10, 'priority_score')
    
    # Create a scatter plot for priority vs urgency
    fig_scatter = px.scatter(
        top_tickets,
        x='priority_score',
        y='resource_urgency',
        size='priority_score',
        color='priority_score',
        hover_data=['ticket_id', 'description'],
        title="Priority Score vs Resource Urgency",
        color_continuous_scale="Reds"
    )
    fig_scatter.update_layout(
        title_font_size=18,
        font=dict(size=12),
        height=400
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Enhanced table
    st.dataframe(top_tickets, use_container_width=True, height=400)

def display_generic_table(df):
    """Display any table in a generic format"""
    st.header("📊 Data Table")
    st.dataframe(df, use_container_width=True)
    
    # Basic statistics
    st.subheader("📈 Basic Statistics")
    st.write(f"**Rows:** {len(df)}")
    st.write(f"**Columns:** {len(df.columns)}")
    
    if len(df) > 0:
        st.write("**Column Types:**")
        st.write(df.dtypes)

if __name__ == "__main__":
    main()
    
    # Add a beautiful footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 10px; margin-top: 2rem;">
        <h3 style="margin: 0; color: white;">🎫 AI Ticket Classification Dashboard</h3>
        <p style="margin: 0.5rem 0; opacity: 0.9;">Powered by Databricks AI Functions & Streamlit</p>
        <p style="margin: 0; font-size: 0.9rem; opacity: 0.8;">Transform your ticket data into actionable business insights</p>
    </div>
    """, unsafe_allow_html=True)
