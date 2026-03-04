import streamlit as st

st.title("🏆 Chennai Open Chess Championship")

st.write("""
Date: 28 March 2026  
Mode: Online  
Platform: Chess.com  
Format: Rapid
""")

st.divider()

st.subheader("📝 Register Now")

st.link_button(
    "Open Registration Form",
    "https://docs.google.com/forms/d/e/1FAIpQLSd8FKhx8SFzMnJxrstoErtyNfKMJm92otwC7DTpr3LsaFmCnw/viewform?usp=sharing&ouid=116092041594100890090",
    use_container_width=True
)
