# app.py - Streamlit Dashboard for Ethiopian Financial Inclusion
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# -----------------------------
# 1. Load Data
# -----------------------------
project_root = Path(__file__).parent
data_file = project_root / "data" / "processed" / "ethiopia_fi_unified_data_enriched.xlsx"

try:
    df = pd.read_excel(data_file, sheet_name="ethiopia_fi_unified_data", engine="openpyxl")
    impact_links = pd.read_excel(data_file, sheet_name="Impact_sheet", engine="openpyxl")
except FileNotFoundError:
    st.error(f"Data file not found at '{data_file}'. Please check path.")
    st.stop()

# Ensure numeric fiscal_year
df['fiscal_year'] = pd.to_numeric(df['fiscal_year'], errors='coerce')
latest_year = int(df['fiscal_year'].max())

# -----------------------------
# 2. Sidebar Navigation
# -----------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Trends", "Event Impacts", "Forecasts"])

# -----------------------------
# 3. Overview Page
# -----------------------------
if page == "Overview":
    st.title("Ethiopia Financial Inclusion - Overview")
    
    col1, col2, col3 = st.columns(3)
    acc_ownership = df.loc[df['fiscal_year']==latest_year, 'ACC_OWNERSHIP'].values
    acc_mm = df.loc[df['fiscal_year']==latest_year, 'ACC_MM_ACCOUNT'].values
    gen_gap = df.loc[df['fiscal_year']==latest_year, 'GEN_GAP_ACC'].values

    col1.metric("Account Ownership (%)", f"{acc_ownership[0]:.2f}" if len(acc_ownership) > 0 else "N/A")
    col2.metric("Mobile Money Accounts (%)", f"{acc_mm[0]:.2f}" if len(acc_mm) > 0 else "N/A")
    col3.metric("Gender Gap in Accounts (%)", f"{gen_gap[0]:.2f}" if len(gen_gap) > 0 else "N/A")

    st.markdown("### Key Insights")
    st.markdown("""
    - Account ownership shows steady growth, but gaps remain between genders.
    - Mobile money adoption continues to expand rapidly.
    - Event-based interventions (Telebirr launch, NFIS2 policies) are expected to drive future growth.
    """)

# -----------------------------
# 4. Trends Page
# -----------------------------
elif page == "Trends":
    st.title("Trends Over Time")
    
    indicator_options = ['ACC_OWNERSHIP', 'ACC_MM_ACCOUNT', 'USG_TELEBIRR_USERS', 'USG_P2P_COUNT']
    selected_indicators = st.multiselect(
        "Select indicators to plot",
        options=indicator_options,
        default=['ACC_OWNERSHIP', 'ACC_MM_ACCOUNT']
    )

    if selected_indicators:
        plt.figure(figsize=(10,5))
        for ind in selected_indicators:
            if ind in df.columns:
                plt.plot(df['fiscal_year'], df[ind], 'o-', label=ind)
        plt.xlabel("Fiscal Year")
        plt.ylabel("Value")
        plt.title("Financial Inclusion Indicators Over Time")
        plt.legend()
        st.pyplot(plt.gcf())
        plt.clf()

# -----------------------------
# 5. Event Impacts Page
# -----------------------------
elif page == "Event Impacts":
    st.title("Event Impacts on Financial Inclusion")
    
    if not impact_links.empty:
        st.markdown("### Events and Their Estimated Impacts")
        display_cols = ['parent_id', 'related_indicator', 'impact_direction', 'impact_magnitude', 'lag_months', 'evidence_basis']
        st.dataframe(impact_links[display_cols])
        
        st.markdown("#### Event-Indicator Heatmap (placeholder)")
        st.info("Visualize event impact matrix here using heatmaps or time series.")
    else:
        st.warning("No impact link data available.")

# -----------------------------
# 6. Forecasts Page
# -----------------------------
elif page == "Forecasts":
    st.title("Forecast: Account Ownership 2025-2027")

    # Use the Task 4 forecast as example
    forecast_df = pd.DataFrame({
        'year': [2025, 2026, 2027],
        'ACC_OWNERSHIP': [61.58, 65.15, 68.73]
    })

    st.table(forecast_df)

    # Forecast plot
    plt.figure(figsize=(8,4))
    if 'ACC_OWNERSHIP' in df.columns:
        plt.plot(df['fiscal_year'], df['ACC_OWNERSHIP'], 'o-', label="Historical ACC_OWNERSHIP")
    plt.plot(forecast_df['year'], forecast_df['ACC_OWNERSHIP'], 's--', label="Forecast")
    plt.xlabel("Year")
    plt.ylabel("Account Ownership (%)")
    plt.title("Forecast of Account Ownership")
    plt.legend()
    st.pyplot(plt.gcf())
    plt.clf()

# -----------------------------
# 7. Data Download
# -----------------------------
st.sidebar.header("Download Data")
st.sidebar.download_button(
    label="Download Processed Data",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name="ethiopia_fi_processed_data.csv",
    mime="text/csv"
)
