import streamlit as st

st.set_page_config(page_title="🪐 Explore the Planets", layout="wide")

st.title("🪐 Explore the Planets in Our Solar System!")
st.markdown("Welcome to your **Summer Coding + Space Project!** Click on each planet to learn fun facts and explore the wonders of our solar system. 🌌")

planets = [
    {
        "name": "Mercury",
        "emoji": "☿️",
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Mercury_in_true_color.jpg",
        "facts": {
            "Position": "1st planet from the Sun",
            "Moons": "None",
            "Length of Day": "59 Earth days",
            "Temperature": "Very hot (day) & freezing (night)",
        },
        "fun_fact": "Mercury has no atmosphere, so it can’t trap heat!"
    },
    {
        "name": "Venus",
        "emoji": "♀️",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e5/Venus-real_color.jpg",
        "facts": {
            "Position": "2nd planet from the Sun",
            "Moons": "None",
            "Length of Day": "243 Earth days",
            "Temperature": "Hottest planet in the solar system",
        },
        "fun_fact": "A day on Venus is longer than its year!"
    },
    {
        "name": "Earth",
        "emoji": "🌍",
        "image": "https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg",
        "facts": {
            "Position": "3rd planet from the Sun",
            "Moons": "1 (The Moon!)",
            "Length of Day": "24 hours",
            "Temperature": "Just right for life 🌱",
        },
        "fun_fact": "Earth is the only known planet with life!"
    },
    {
        "name": "Mars",
        "emoji": "🔴",
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg",
        "facts": {
            "Position": "4th planet from the Sun",
            "Moons": "2 (Phobos & Deimos)",
            "Length of Day": "24.6 hours",
            "Temperature": "Cold and dusty",
        },
        "fun_fact": "Mars is home to the tallest volcano in the solar system: Olympus Mons!"
    },
    {
        "name": "Jupiter",
        "emoji": "🟠",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e2/Jupiter.jpg",
        "facts": {
            "Position": "5th planet from the Sun",
            "Moons": "Over 90!",
            "Length of Day": "10 hours",
            "Temperature": "Super cold gas giant",
        },
        "fun_fact": "Jupiter has a giant storm called the Great Red Spot!"
    },
    {
        "name": "Saturn",
        "emoji": "🪐",
        "image": "https://upload.wikimedia.org/wikipedia/commons/c/c7/Saturn_during_Equinox.jpg",
        "facts": {
            "Position": "6th planet from the Sun",
            "Moons": "145+ known",
            "Length of Day": "10.7 hours",
            "Temperature": "Very cold",
        },
        "fun_fact": "Saturn’s rings are made of ice and rock chunks!"
    },
    {
        "name": "Uranus",
        "emoji": "🌀",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Uranus2.jpg",
        "facts": {
            "Position": "7th planet from the Sun",
            "Moons": "27 known",
            "Length of Day": "17 hours",
            "Temperature": "Coldest planet in the solar system",
        },
        "fun_fact": "Uranus spins on its side!"
    },
    {
        "name": "Neptune",
        "emoji": "🔵",
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/56/Neptune_Full.jpg",
        "facts": {
            "Position": "8th planet from the Sun",
            "Moons": "14 known",
            "Length of Day": "16 hours",
            "Temperature": "Very cold with supersonic winds",
        },
        "fun_fact": "Neptune has the strongest winds in the solar system!"
    },
]

cols = st.columns(2)
for i, planet in enumerate(planets):
    with cols[i % 2]:
        st.markdown(f"### {planet['emoji']} {planet['name']}")
        st.image(planet["image"], width=250)
        with st.expander("Click to learn more"):
            for key, value in planet['facts'].items():
                st.write(f"**{key}**: {value}")
            st.markdown(f"💡 **Fun Fact**: {planet['fun_fact']}")

st.markdown("---")
st.markdown("🚀 Keep learning, exploring, and coding! You're doing an amazing job! 🌟")
