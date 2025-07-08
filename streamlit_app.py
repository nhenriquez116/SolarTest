import streamlit as st
import pandas as pd

st.title("🌌 What's Your Weight on Other Planets?")

# Ask for user input
# Ask for user inputTest
#new
earth_weight = st.number_input("Enter your weight on Earth (in pounds or kg):", min_value=0.0, step=1.0)

# Gravitational factors relative to Earth
gravity = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Earth": 1.00,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Uranus": 0.92,
    "Neptune": 1.19,
    "Pluto": 0.06  # Optional
}

if earth_weight > 0:
    results = {
        planet: round(earth_weight * factor, 2)
        for planet, factor in gravity.items()
    }

    df = pd.DataFrame.from_dict(results, orient='index', columns=["Your Weight"])
    st.subheader("💫 Your Weight on Each Planet:")
    st.dataframe(df)

    st.bar_chart(df)

else:
    st.info("Please enter a weight greater than 0.")

