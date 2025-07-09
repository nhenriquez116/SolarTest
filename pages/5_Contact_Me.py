import streamlit as st

st.set_page_config(page_title="📬 Contact Me", page_icon="📬")

st.title("📬 Let's Chat!")
st.markdown("""
Hey there! 👋  
I’m super excited to hear from you. Got cool ideas, feedback, or just want to say hi?  
Fill out the form below and let’s keep in touch! 🚀  
""")

with st.form("contact_form"):
    name = st.text_input("Your Name ✍️", max_chars=50)
    email = st.text_input("Your Email 📧", max_chars=50)
    message = st.text_area("Your Message 💬", max_chars=500, help="Type anything you want to share!")
    submitted = st.form_submit_button("Send Message 📤")

if submitted:
    if not name or not email or not message:
        st.error("Oops! Please fill out all the fields to send your message.")
    else:
        # Normally here you would send the data to your email or backend.
        # Since we can't do that here, let's show a fun thank you message.
        st.success(f"Thanks so much, {name}! Your message has been sent. 🌟")
        st.balloons()
        st.write("I'll get back to you as soon as I can! Meanwhile, keep being awesome! 😎")

st.markdown("---")
st.write("💡 PS: If you want to reach me directly, you can email me at: **nhenriquez116@gmail.com**")
