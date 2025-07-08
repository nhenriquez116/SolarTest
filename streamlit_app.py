import streamlit as st

# Set page config
st.set_page_config(
    page_title="🌞 My Summer Solar System Coding Project 🚀",
    page_icon="🌌",
    layout="centered"
)

# Title with emoji
st.markdown("<h1 style='text-align: center; color: orange;'>🌞 My Summer Solar System Coding Project 🚀</h1>", unsafe_allow_html=True)

# Fun welcome message
st.markdown("""
<div style='text-align: center; font-size: 20px;'>
Welcome to my <span style='color: gold;'><b>summer journey</b></span> through space and code! 🌍💻
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Project intro
st.markdown("""
### 🌟 **Why I Built This Project**
This summer, I'm combining **science** 🧪 and **computer programming** 👩‍💻 to:
- Learn awesome facts about the **planets** in our **Solar System** 🪐
- Build cool interactive **web apps** using **Streamlit**
- Practice using **VS Code** and **GitHub** like real developers 🚀
""")

st.markdown("""
### 🛠️ **What You’ll Find Here**
This project has multiple pages with fun tools and activities:
- 🌍 **How old you'd be on other planets**
- ⚖️ **Your weight on Jupiter or the Moon**
- 🛰️ **Fun facts about each planet**
- 🧑‍🚀 More coming soon as I learn!
""")

st.markdown("""
### 👨‍💻 **Tech I'm Using**
- [Streamlit](https://streamlit.io/) for building apps 💡  
- [GitHub](https://github.com/) to save and share my code 🌐  
- [VS Code](https://code.visualstudio.com/) as my coding notebook 📓
""")

st.markdown("---")

# Closing message
st.markdown("""
<div style='text-align: center; font-size: 18px; color: green;'>
<b>Click the menu on the left to explore the universe with me!</b> 🌠<br>
Let’s code and learn something cosmic together! 🛸
</div>
""", unsafe_allow_html=True)
