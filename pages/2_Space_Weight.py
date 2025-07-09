import streamlit as st
import pandas as pd

# Page setup
st.set_page_config(page_title="🌎 Planet Weight Explorer", page_icon="🪐", layout="centered")

# Title with fun style
st.markdown("<h1 style='text-align: center; color: #6A5ACD;'>🪐 What’s Your Weight on Other Planets?</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #FF69B4;'>Find out how gravity changes your weight across the solar system!</h4>", unsafe_allow_html=True)

# Input weight
earth_weight = st.number_input(
    "👣 Enter your weight on Earth (in pounds or kg):",
    min_value=0.0,
    step=1.0,
    help="Try putting in your real weight or guess one!"
)

# Gravitational multipliers
gravity = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Earth": 1.00,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Uranus": 0.92,
    "Neptune": 1.19,
    "Pluto": 0.06  # still fun for kids!
}

# Process and display
if earth_weight > 0:
    results = {
        planet: round(earth_weight * factor, 2)
        for planet, factor in gravity.items()
    }

    df = pd.DataFrame.from_dict(results, orient='index', columns=["Your Weight"])

    st.markdown("### 🌟 Your Weight Across the Solar System")
    st.dataframe(df.style.format({"Your Weight": "{:.2f}"}).highlight_max(axis=0, color="lightgreen"))

    st.markdown("### 📊 Gravity Comparison Chart")
    st.bar_chart(df)

    st.markdown("---")
    st.markdown("<div style='text-align: center;'>💡 <em>Cool Fact:</em> You would weigh the most on <strong>Jupiter</strong> because it's the biggest planet with the strongest gravity!</div>", unsafe_allow_html=True)

else:
    st.info("⬆️ Enter a weight above to start your space adventure!")

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>🚀 Keep exploring the stars! Science is awesome. 🌌</div>", unsafe_allow_html=True)
