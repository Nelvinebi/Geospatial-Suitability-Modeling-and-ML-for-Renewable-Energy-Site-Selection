import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# Page configuration
st.set_page_config(
    page_title="Renewable Energy Suitability Dashboard",
    layout="wide"
)

# Title
st.title("Renewable Energy Site Suitability Analytics Platform")

st.markdown(
"""
This dashboard analyzes **renewable energy site suitability**
using geospatial data and machine learning.
"""
)

# Load dataset
df = pd.read_excel("data.xlsx")

# ===============================
# Sidebar
# ===============================

st.sidebar.header("Dashboard Controls")

selected_class = st.sidebar.selectbox(
    "Select Suitability Class",
    df["suitability_class"].unique()
)

wind_filter = st.sidebar.slider(
    "Minimum Wind Speed",
    float(df["wind_speed"].min()),
    float(df["wind_speed"].max()),
    float(df["wind_speed"].mean())
)

solar_filter = st.sidebar.slider(
    "Minimum Solar Irradiance",
    float(df["solar_irradiance"].min()),
    float(df["solar_irradiance"].max()),
    float(df["solar_irradiance"].mean())
)

# Filter dataset
filtered_df = df[
    (df["suitability_class"] == selected_class) &
    (df["wind_speed"] >= wind_filter) &
    (df["solar_irradiance"] >= solar_filter)
]

# ===============================
# Key Metrics
# ===============================

st.subheader("Key Dataset Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Locations", len(df))
col2.metric("Filtered Locations", len(filtered_df))
col3.metric("Average Wind Speed", round(df["wind_speed"].mean(),2))

# ===============================
# Geospatial Map
# ===============================

st.subheader("Renewable Energy Suitability Map")

fig = px.scatter_mapbox(
    filtered_df,
    lat="latitude",
    lon="longitude",
    color="suitability_class",
    size="wind_speed",
    zoom=5,
    mapbox_style="carto-positron",
    title="Spatial Distribution of Suitable Renewable Energy Locations"
)

st.plotly_chart(fig, use_container_width=True)

# ===============================
# Environmental Data Analysis
# ===============================

st.subheader("Environmental Variable Distribution")

col1, col2 = st.columns(2)

with col1:
    fig2 = px.histogram(
        df,
        x="wind_speed",
        title="Wind Speed Distribution"
    )
    st.plotly_chart(fig2)

with col2:
    fig3 = px.histogram(
        df,
        x="solar_irradiance",
        title="Solar Irradiance Distribution"
    )
    st.plotly_chart(fig3)

# ===============================
# Machine Learning Prediction
# ===============================

st.subheader("Renewable Energy Suitability Prediction")

try:
    model = joblib.load("model/suitability_model.pkl")

    wind_input = st.slider("Wind Speed", 0.0, 20.0, 5.0)
    solar_input = st.slider("Solar Irradiance", 0.0, 1000.0, 500.0)
    elevation_input = st.slider("Elevation", 0.0, 1000.0, 100.0)

    if st.button("Predict Suitability"):

        prediction = model.predict(
            [[wind_input, solar_input, elevation_input]]
        )

        st.success(f"Predicted Suitability Class: {prediction[0]}")

except:
    st.warning("ML model not yet uploaded.")

# ===============================
# Scenario Simulation
# ===============================

st.subheader("Renewable Energy Scenario Simulation")

scenario_wind = st.slider(
    "Scenario Wind Speed",
    0.0, 20.0, 8.0
)

scenario_solar = st.slider(
    "Scenario Solar Irradiance",
    0.0, 1000.0, 700.0
)

scenario_score = scenario_wind * 0.6 + scenario_solar * 0.4

st.write("Suitability Scenario Score:", scenario_score)