import streamlit as st
import requests
from datetime import date

# Config
st.set_page_config(page_title="NASA APOD Viewer", layout="centered")
st.title("🌌 NASA Astronomy Picture of the Day")

# API setup
API_KEY = "DEMO_KEY"  # Replace with your own key if needed
API_URL = "https://api.nasa.gov/planetary/apod"

# User input: Date selection
selected_date = st.date_input("Select a date:", value=date.today(), min_value=date(1995, 6, 16), max_value=date.today())
params = {"api_key": API_KEY, "date": selected_date.isoformat()}

# Fetch APOD
@st.cache_data
def fetch_apod(params):
    response = requests.get(API_URL, params=params)
    return response.json()

data = fetch_apod(params)

# Display
st.header(data.get("title", "No Title"))
st.subheader(data.get("date", ""))

if data.get("media_type") == "image":
    st.image(data.get("url"), use_container_width=True)
elif data.get("media_type") == "video":
    st.video(data.get("url"))
else:
    st.warning("Unsupported media type.")

st.markdown("### 📖 Explanation")
st.write(data.get("explanation", "No explanation available."))

# Optional: show copyright
if "copyright" in data:
    st.markdown(f"© {data['copyright']}")
