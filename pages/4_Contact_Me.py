import streamlit as st

st.set_page_config(page_title="Contact Me", page_icon="📬")

st.title("📬 Contact Me")
st.write("I'd love to hear your thoughts or feedback. Fill out this form below!")

# FormSubmit endpoint (your email, but hashed/hidden)
form_action = "https://formsubmit.co/nhenriquez116@gmail.com"

# HTML form inside Streamlit
contact_form = f"""
    <form action="{form_action}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required><br><br>
        <input type="email" name="email" placeholder="Your email" required><br><br>
        <textarea name="message" placeholder="Your message here..." rows="5" required></textarea><br><br>
        <button type="submit">Send Message</button>
    </form>
"""

# Render HTML form
st.markdown(contact_form, unsafe_allow_html=True)
