import streamlit as st
import pandas as pd
from databricks import sql
from databricks.sdk.core import Config
import os

# Page configuration
st.set_page_config(
    page_title="AI Ticket Classification Dashboard",
    page_icon="🎫",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Databricks configuration
cfg = Config()

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
    st.title("🎫 AI Ticket Classification Dashboard")
    st.markdown("**Transform AI analysis into actionable business insights**")
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Get warehouse ID
        warehouse_id = get_warehouse_id()
        if warehouse_id:
            st.success(f"✅ Warehouse ID: {warehouse_id}")
            http_path = f"/sql/1.0/warehouses/{warehouse_id}"
        else:
            st.warning("⚠️ No warehouse ID found in environment")
            http_path = st.text_input(
                "Enter Databricks HTTP Path:",
                placeholder="/sql/1.0/warehouses/xxxxxx",
                help="Set DATABRICKS_WAREHOUSE_ID environment variable for automatic detection"
            )
        
        # Table selection
        st.subheader("📊 Data Sources")
        table_options = [
            "quickstart_catalog_vkm_external.classify_tickets.ai_showcase_results",
            "quickstart_catalog_vkm_external.classify_tickets.dashboard_priority_distribution",
            "quickstart_catalog_vkm_external.classify_tickets.dashboard_system_health",
            "quickstart_catalog_vkm_external.classify_tickets.dashboard_resource_allocation"
        ]
        
        selected_table = st.selectbox(
            "Select Table:",
            table_options,
            help="Choose which dashboard data to display"
        )
    
    # Main content area
    if http_path and selected_table:
        try:
            # Establish connection
            with st.spinner("Connecting to Databricks..."):
                conn = get_connection(http_path)
            
            # Read data
            with st.spinner("Loading data..."):
                df = read_table(selected_table, conn)
            
            # Display data based on table type
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
            st.error(f"❌ Error connecting to Databricks: {str(e)}")
            st.info("💡 Make sure you have the correct warehouse ID and proper permissions")
    else:
        st.warning("⚠️ Please provide both the warehouse path and select a table to load data.")

def display_ai_showcase_results(df):
    """Display AI showcase results with business insights"""
    st.header("🤖 AI Analysis Results")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Tickets", len(df))
    
    with col2:
        urgent_count = len(df[df['ai_priority_classification'] == 'Urgent Priority'])
        st.metric("Urgent Tickets", urgent_count)
    
    with col3:
        high_risk = len(df[df['urgency_level'].str.contains('urgent|asap|high', case=False, na=False)])
        st.metric("High Risk", high_risk)
    
    with col4:
        unique_systems = df['affected_systems'].nunique()
        st.metric("Systems Affected", unique_systems)
    
    # Priority distribution chart
    st.subheader("📊 Priority Distribution")
    priority_counts = df['ai_priority_classification'].value_counts()
    st.bar_chart(priority_counts)
    
    # Detailed table
    st.subheader("📋 Detailed Analysis")
    st.dataframe(df, use_container_width=True)

def display_priority_distribution(df):
    """Display priority distribution with charts"""
    st.header("📈 Priority Distribution Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Distribution by Count")
        st.bar_chart(df.set_index('priority_level')['ticket_count'])
    
    with col2:
        st.subheader("Distribution by Percentage")
        st.bar_chart(df.set_index('priority_level')['percentage'])
    
    # Color-coded table
    st.subheader("📊 Priority Breakdown")
    st.dataframe(df, use_container_width=True)

def display_system_health(df):
    """Display system health analysis"""
    st.header("🏥 System Health Analysis")
    
    # Health status distribution
    health_counts = df['health_status'].value_counts()
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Health Status Distribution")
        st.bar_chart(health_counts)
    
    with col2:
        st.subheader("Urgent Tickets by System")
        urgent_systems = df[df['urgent_tickets'] > 0]
        if not urgent_systems.empty:
            st.bar_chart(urgent_systems.set_index('system_name')['urgent_tickets'])
        else:
            st.info("No urgent tickets found")
    
    # System health table
    st.subheader("📊 System Health Details")
    st.dataframe(df, use_container_width=True)

def display_resource_allocation(df):
    """Display resource allocation recommendations"""
    st.header("🎯 Resource Allocation Recommendations")
    
    # Priority score distribution
    st.subheader("Priority Score Distribution")
    st.bar_chart(df['priority_score'].value_counts().sort_index())
    
    # Resource urgency breakdown
    urgency_counts = df['resource_urgency'].value_counts()
    st.subheader("Resource Urgency Breakdown")
    st.bar_chart(urgency_counts)
    
    # Top priority tickets
    st.subheader("🚨 Top Priority Tickets")
    top_tickets = df.nlargest(10, 'priority_score')
    st.dataframe(top_tickets, use_container_width=True)

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
