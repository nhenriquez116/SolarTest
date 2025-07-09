import streamlit as st
import requests
from datetime import datetime, date
import pytz

# Set timezone (use full name like 'US/Eastern', not 'EST')
eastern = pytz.timezone("US/Eastern")
now_eastern = datetime.now(eastern)
local_today = now_eastern.date()

# Show it (for debugging)
# st.write(f"Local (Eastern) time: {now_eastern}")
# st.write(f"Local (Eastern) date: {local_today}")

# API setup
API_KEY = "DEMO_KEY"
API_URL = "https://api.nasa.gov/planetary/apod"

# User input
selected_date = st.date_input(
    "Select a date:",
    value=local_today,
    min_value=date(1995, 6, 16),
    max_value=local_today
)

params = {"api_key": API_KEY, "date": selected_date.isoformat()}

@st.cache_data
def fetch_apod(params):
    response = requests.get(API_URL, params=params)
    return response.json()

data = fetch_apod(params)

# Display
st.title("🌌 NASA Astronomy Picture of the Day")
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

if "copyright" in data:
    st.markdown(f"© {data['copyright']}")
