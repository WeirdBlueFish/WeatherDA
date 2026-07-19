import streamlit as st
import plotly.express as px
import pandas as pd 
import numpy as np
import jdatetime
import httpx
import matplotlib.pyplot as plt
import seaborn as sns

def to_shamsi(BaseDate):
    py_date = BaseDate.date()
    shamsi = jdatetime.date.fromgregorian(date=py_date)

    return shamsi

st.set_page_config(page_title="Weather Dashboard", layout='wide')
st.title("🌍 Latitude & Longitude Data Analyse")

@st.cache_data
def fetch_data(lat, lon):
    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {
    'latitude': lat,
    'longitude': lon,
    'start_date': '2010-01-01',
    'end_date': "2026-07-18",
    'daily': "temperature_2m_max,temperature_2m_min,temperature_2m_mean",
    'timezone': 'Asia/Tehran'
            }   
    
    response = httpx.get(url=url, params=params, timeout=10.0)
    data = response.json()
    daily = data['daily']

    df = pd.DataFrame(
        {"date": daily['time'],
        "min_temp": daily['temperature_2m_min'],
        "max_temp": daily['temperature_2m_max'],
        "mean_temp": daily['temperature_2m_mean']}
                    )
    df['date'] = pd.to_datetime(df['date'])

    df['shamsi'] = df['date'].apply(lambda x: to_shamsi(x).strftime('%Y-%m-%d'))
    df['month_num'] = df['date'].apply(lambda x: to_shamsi(x).strftime('%m'))
    df['shamsi_month'] = df['date'].apply(lambda x: to_shamsi(x).strftime('%B'))
    df['day_of_year'] = df['date'].apply(lambda x: to_shamsi(x).strftime('%j'))
    df['day_of_week'] = df['date'].apply(lambda x: to_shamsi(x).strftime('%A'))
    df['day_num_of_week'] = df['date'].apply(lambda x: to_shamsi(x).strftime('%w'))
    df['day_num_of_month'] = df['date'].apply(lambda x: to_shamsi(x).day)

    return df


st.write("### Enter lat & lon: ")

col1, col2 = st.columns(2)

with col1:
    user_lat = st.number_input("Latitude:", value=40.730610, format='%.6f')
with col2:
    user_lon = st.number_input("Longitude:", value=-73.935242, format='%.4f')

if st.button("Download Data From API"):
    with st.spinner("Downloading..."):
        df = fetch_data(user_lat, user_lon)

        st.session_state['api_data'] = df
        st.success("✅ Succefully Fetched!")

st.divider()

# _____________________

if 'api_data' in st.session_state:
    st.write("### Data Visualization")
    
    df = st.session_state['api_data']
    
    chart_type = st.selectbox(
        "Select a chart to view:",
        ["Calendar Heatmap (Average Temp)", "Temperature Distribution by Month (Boxplot)"]
    )
    
    month_order = ['Farvardin', 'Ordibehesht', 'Khordad', 'Tir', 'Mordad', 'Shahrivar', 
                   'Mehr', 'Aban', 'Azar', 'Dey', 'Bahman', 'Esfand']
    
    if chart_type == "Calendar Heatmap (Average Temp)":
        
        heatmap_data = df.pivot_table(index='shamsi_month', columns='day_num_of_month', values='mean_temp')

        months_orders = [
            'Farvardin', 'Ordibehesht', 'Khordad', 'Tir', 'Mordad', 'Shahrivar',
            'Mehr', 'Aban', 'Azar', 'Dey', 'Bahman', 'Esfand'
        ]
        existing_month = [m for m in months_orders if m in heatmap_data.index]
        heatmap_data = heatmap_data.reindex(existing_month)
        
        fig, ax = plt.subplots(figsize=(20, 8))

        sns.heatmap(
            data=heatmap_data,
            cmap='RdYlBu_r',
            linewidths=0.1,
            linecolor='white',
            ax=ax  
        )

        ax.set_title("Temp Calendar", fontsize=16)
        ax.set_xlabel("Day", fontsize=12)
        ax.set_ylabel("Month", fontsize=12)

        st.pyplot(fig)
        
    elif chart_type == "Temperature Distribution by Month (Boxplot)":
        
        fig = px.box(
            df, 
            x='shamsi_month', 
            y='mean_temp', 
            color='shamsi_month',
            title="Temperature Distribution by Shamsi Month",
            labels={'shamsi_month': 'Shamsi Month', 'mean_temp': 'Mean Temp (°C)'},
            category_orders={"shamsi_month": month_order} 
        )
        st.plotly_chart(fig, use_container_width=True)

    with st.expander("Show Raw Data"):
        st.dataframe(df)