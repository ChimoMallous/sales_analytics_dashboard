import streamlit as st
import pandas as pd
import numpy as np
from analytics import calculate_kpis
from data_processing import load_sample_data

# Set page configuration
st.set_page_config(page_title="Sales_Analytics_Dashboard", layout="wide")
st.title("Sales Analytics Dashboard")
df = pd.DataFrame()

# Add button to load sample data
if st.button("Load Sample Data"):
    with st.spinner("Loading sample data..."):
        df = load_sample_data()

# Main dashboard, only show if data is loaded
if not df.empty:
    st.subheader("Sales Data Overview")
    main_col1, main_col2 = st.columns(2)

    with main_col1:
        with st.expander("View Data Head (5 rows)"):
            st.dataframe(df.head(5))

        # Calculate and display KPIs
        st.subheader("Key Performance Indicators (KPIs)")
        kpis = calculate_kpis(df)
        kpi_col1, kpi_col2, kpi_col3 = st.columns(3)
        kpi_col1.metric("Total Revenue", f"${kpis['total_revenue']:,.2f}")
        kpi_col2.metric("Total Profit", f"${kpis['total_profit']:,.2f}")
        kpi_col3.metric("Total Orders", f"{kpis['total_orders']:,}")      
