import streamlit as st

def render_right_nav(selected_page):
    if selected_page == "B2B_VA":
        st.markdown("### Sections")
        st.markdown("""
- [Overview](#overview)
- [Use case](#usecase)
- [Integrate Methods](#integrate)
- [Sandbox](#sandbox)
- [API Reference](#api)
- [Security](#security)
- [Webhook](#webhook)
- [Error Codes](#errors)
""")
