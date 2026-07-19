# 🌦️ Weather Analysis Dashboard

This project is an interactive, user-friendly dashboard designed for fetching, processing, and visualizing historical weather data. By inputting geographic coordinates (latitude and longitude), users can explore temperature patterns through line charts, boxplots, and calendar heatmaps.

## ✨ Key Features
*   **Live Data Fetching:** Connects to the powerful Open-Meteo API to retrieve historical temperature data.
*   **Calendar Conversion:** Full support for converting Gregorian dates to Jalali (Shamsi) using the `jdatetime` library.
*   **Advanced Visualizations:**
    *   Interactive charts with **Plotly** to analyze temperature trends over time.
    *   Calendar heatmaps using **Seaborn** & **Matplotlib** to observe seasonal and daily temperature patterns.
*   **Modern User Interface:** Developed with **Streamlit** for a seamless, browser-based experience.
*   **Smart Caching:** Utilizes `@st.cache_data` to optimize performance and minimize redundant API calls.

## 🛠 Technologies Used
*   **Python 3.x**
*   **Streamlit** (Web framework)
*   **Pandas & NumPy** (Data processing and analysis)
*   **Plotly, Seaborn & Matplotlib** (Data visualization)
*   **httpx** (API requests)
*   **jdatetime** (Date conversion)

## 🚀 Installation & Setup

1. Clone the repository or download the files:
```bash
git clone [https://github.com/WeirdBlueFish/WeatherDA]
cd [WeatherDA]
```

2. Install the required dependencies:
```Bash
pip install requirements.txt
```

3. Run the application:
```Bash
streamlit run src/app.py
```
Your default web browser will open automatically and display the dashboard.

## 📊 How to Use

0. Once the app is running, enter your desired Latitude and Longitude in the provided input fields.
1. Click the "Download Data From API" button to fetch and process the weather data.
2. Use the dropdown menu to switch between different visualization modes (e.g., Line Chart, Boxplot, or Calendar Heatmap).


## 💡 Future Road Map
. [ ] Add the ability to compare two different geographic locations on the same chart.

. [ ] Implement Machine Learning models for short-term temperature forecasting.

. [ ] Allow users to export processed data as CSV or Excel files.


### 📝 License
This project is licensed under the MIT License.
Made with ❤️ by Farbod Mehrgan
