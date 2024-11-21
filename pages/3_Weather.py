import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt  # For dynamic graphs

# NEW: Set page configuration
st.set_page_config(
    page_title="Weather Forecast",
    page_icon="🌤",
    layout="wide",
)

# App Title
st.title("Weather Forecast App 🌤")
st.write("Get the latest weather forecast for your location.")

# User Inputs
latitude = st.number_input("Enter Latitude", value=37.7749, format="%.4f")
longitude = st.number_input("Enter Longitude", value=-122.4194, format="%.4f")
days = st.slider("Select Forecast Duration (1-7 days)", 1, 7, value=3)  # NEW

if st.button("Get Weather Forecast"):
    # Fetch Data from Open-Meteo API
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,temperature_2m_min",
        "timezone": "auto",
        "forecast_days": days,
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        # Data Processing
        time = data["daily"]["time"]
        temp_max = data["daily"]["temperature_2m_max"]
        temp_min = data["daily"]["temperature_2m_min"]

        forecast = pd.DataFrame({
            "Date": time,
            "Max Temperature (°C)": temp_max,
            "Min Temperature (°C)": temp_min,
        })

        # NEW: Dynamic Graph
        st.subheader("Temperature Forecast")
        fig, ax = plt.subplots()
        ax.plot(time, temp_max, label="Max Temperature", color="red")
        ax.plot(time, temp_min, label="Min Temperature", color="blue")
        ax.set_xlabel("Date")
        ax.set_ylabel("Temperature (°C)")
        ax.set_title("Daily Temperature Forecast")
        ax.legend()
        st.pyplot(fig)

        # NEW: Display Data as Table
        st.subheader("Forecast Data")
        st.dataframe(forecast)

    else:
        st.error("Failed to fetch data. Please try again.")

