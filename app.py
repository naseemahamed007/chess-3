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
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>🏆 Tournaments</h3>
        <p>Professional Events</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>👥 Membership</h3>
        <p>Join Our Academy</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>📞 Contact</h3>
        <p>Get in Touch</p>
    </div>
    """, unsafe_allow_html=True)


st.divider()


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
