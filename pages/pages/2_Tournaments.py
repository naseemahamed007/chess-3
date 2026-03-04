import streamlit as st

st.title("🏆 Tournaments")

st.subheader("Upcoming Event")

st.write("""
### Chennai Open Chess Championship
Date: 28 March 2026  
Mode: Online  
Platform: Chess.com
""")


st.link_button(
    "📝 Register Now",
    "PASTE_YOUR_GOOGLE_FORM_LINK",
    use_container_width=True
)
