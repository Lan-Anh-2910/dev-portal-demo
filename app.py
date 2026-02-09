import streamlit as st
from components.left_nav import render_left_nav
from components.right_nav import render_right_nav
from pages.b2b_va import render_b2b_va

st.set_page_config(
    page_title="Developer Portal Demo",
    layout="wide"
)

if "selected_page" not in st.session_state:
    st.session_state.selected_page = None

left, center, right = st.columns([1.2, 4.5, 1.6])

with left:
    render_left_nav()

with right:
    render_right_nav(st.session_state.selected_page)

with center:
    if st.session_state.selected_page is None:
        st.title("Welcome to Developer Portal")
        st.write("""
Select a product from the left navigation to view API documentation.

This portal provides:
- Integration guides
- Sandbox environment
- API references
- Security & webhook specifications
""")
    elif st.session_state.selected_page == "B2B_VA":
        render_b2b_va()
