import streamlit as st
from components.section_sidebar import render_section_sidebar

st.set_page_config(layout="wide")

center, right = st.columns([4.5, 1.5])

with right:
    render_section_sidebar([
        "Overview",
        "Use case",
        "Integration Methods"
    ])

with center:
    st.title("Virtual Account")
    st.write("VA hub page")
