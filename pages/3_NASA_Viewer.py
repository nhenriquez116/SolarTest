import streamlit as st
import requests
from datetime import datetime, date
import pytz

# Set up timezone to get correct current date
eastern = pytz.timezone("US/Eastern")
now_eastern = datetime.now(eastern)
local_today = now_eastern.date()

# Page config
st.set_page_config(page_title="🚀 NASA Space Pic of the Day!", page_icon="🌠", layout="centered")

# Sidebar with a fun note
st.sidebar.title("🧑‍🚀 Space Explorer Zone")
st.sidebar.markdown("Welcome, young astronaut! 👩‍🚀👨‍🚀\nPick a date and explore the universe!")

# Title with emoji and color
st.markdown("<h1 style='text-align: center; color: #6C63FF;'>🌌 NASA Astronomy Picture of the Day</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #FF6F61;'>A cosmic adventure every day!</h4>", unsafe_allow_html=True)

# Date input
selected_date = st.date_input(
    "📅 Pick a space day to explore!",
    value=local_today,
    min_value=date(1995, 6, 16),
    max_value=local_today
)

# NASA API
API_KEY = "DEMO_KEY"
API_URL = "https://api.nasa.gov/planetary/apod"
params = {"api_key": API_KEY, "date": selected_date.isoformat()}

@st.cache_data
def fetch_apod(params):
    response = requests.get(API_URL, params=params)
    return response.json()

data = fetch_apod(params)

# Display the results
st.markdown(f"### 🛰️ **{data.get('title', 'No Title')}**")
st.markdown(f"**📆 Date:** {data.get('date', '')}")

if data.get("media_type") == "image":
    st.image(data.get("url"), use_container_width=True, caption="📷 Photo from space!")
elif data.get("media_type") == "video":
    st.video(data.get("url"))
else:
    st.warning("😕 This type of media isn't supported today. Try another date!")

# Explanation with icon and style
st.markdown("### 📖 What’s Going On in Space?")
st.write(data.get("explanation", "No explanation available. 🚀"))

# Optional credit
if "copyright" in data:
    st.markdown(f"🌟 *Image Credit:* **{data['copyright']}**")

# Footer fun message
st.markdown("---")
st.markdown("<div style='text-align: center; color: #888;'>Keep exploring, star traveler! 🌠</div>", unsafe_allow_html=True)
