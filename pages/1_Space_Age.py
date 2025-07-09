import pandas as pd
import streamlit as st

# Page setup
st.set_page_config(page_title="🚀 How Old Are You on Other Planets?", page_icon="🪐", layout="centered")

# Page title and intro
st.markdown("<h1 style='text-align: center; color: #20B2AA;'>🪐 How Old Are You on Other Planets?</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #FFA500;'>Let’s travel through the solar system and see how your age changes!</h4>", unsafe_allow_html=True)

# User input
earth_age = st.number_input(
    "🧒 Enter your age on Earth (in years):",
    min_value=0.0,
    step=1.0,
    help="Try putting your real age or test with a number like 100!"
)

# Orbital periods (in Earth years)
orbital_period = {
    "Mercury": 0.24,
    "Venus": 0.62,
    "Earth": 1.00,
    "Mars": 1.88,
    "Jupiter": 11.86,
    "Saturn": 29.46,
    "Uranus": 84.01,
    "Neptune": 164.8,
    "Pluto": 248.6  # Still fun!
}

# Calculate and display results
if earth_age > 0:
    results = {
        planet: round(earth_age / period, 2)
        for planet, period in orbital_period.items()
    }

    df = pd.DataFrame.from_dict(results, orient='index', columns=["Your Age"])

    st.markdown("### 🧭 Your Space Age Chart")
    st.dataframe(df.style.format({"Your Age": "{:.2f}"}).highlight_min(axis=0, color="#FFD700"))

    st.markdown("### 📊 Age on Planets Comparison")
    st.bar_chart(df)

    st.markdown("---")
    st.markdown(
        "<div style='text-align: center;'>"
        "🎉 <b>Fun Fact:</b> If you were on <span style='color: #FF4500;'>Mercury</span>, you'd already be way older! "
        "But on <span style='color: #1E90FF;'>Neptune</span>, you might still be a baby! 👶"
        "</div>", unsafe_allow_html=True
    )

else:
    st.info("🚨 Enter your age above to begin your space-time journey!")

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>🌌 Time is different everywhere in space... keep exploring!</div>", unsafe_allow_html=True)
