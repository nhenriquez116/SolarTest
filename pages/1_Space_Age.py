import pandas as pd
import streamlit as st

st.title("🪐 How Old Are You on Other Planets?")

# Ask for user input
earth_age = st.number_input("Enter your age on Earth (in years):", min_value=0.0, step=1.0)

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
    "Pluto": 248.6  # Optional
}

if earth_age > 0:
    results = {
        planet: round(earth_age / period, 2)
        for planet, period in orbital_period.items()
    }

    df = pd.DataFrame.from_dict(results, orient='index', columns=["Your Age"])
    st.subheader("👶 Your Age on Each Planet:")
    st.dataframe(df)

    st.bar_chart(df)

else:
    st.info("Please enter an age greater than 0.")
