import streamlit as st

# Page Config
st.set_page_config(
    page_title="Nas Matrix Chess",
    layout="wide"
)

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Hero Section
st.markdown("""
<div class="hero">
    <h1>♟️ Nas Matrix Chess</h1>
    <p>Official Chess Organization</p>
</div>
""", unsafe_allow_html=True)


st.divider()


# Info Cards
import streamlit as st

st.set_page_config(layout="wide")

# CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Hero
st.markdown("""
<div class="hero">
<h1>♟️ Nas Matrix Chess</h1>
<p>Official Chess Organization</p>
</div>
""", unsafe_allow_html=True)

st.divider()


# Navigation Buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏆 Tournaments", use_container_width=True):
        st.switch_page("pages/2_Tournaments.py")

with col2:
    if st.button("👥 Membership", use_container_width=True):
        st.switch_page("pages/3_Membership.py")

with col3:
    if st.button("📞 Contact", use_container_width=True):
        st.switch_page("pages/4_Contact.py")
# About Section
st.markdown("""
## ♟️ About Us

Nas Matrix Chess is a professional chess organization
dedicated to building champions with discipline,
strategy, and excellence.
""")


st.divider()


# Footer
st.markdown("""
<p class="footer">
© 2026 Nas Matrix Chess | All Rights Reserved
</p>
""", unsafe_allow_html=True)
