import streamlit as st
from components.section_sidebar import render_section_sidebar

st.set_page_config(layout="wide")

center, right = st.columns([4.5, 1.5])

with right:
    render_section_sidebar(["Overview", "Use case", "Integration Methods"])

with center:
    st.title("Virtual Account")

    st.markdown('<a name="integration-methods"></a>', unsafe_allow_html=True)
    st.header("Integration Methods")

    st.page_link(
        page="b2b_va_direct_basic",
        label="Direct Merchant / Basic"
    )
    st.page_link(
        page="b2b_va_direct_h2h",
        label="Direct Merchant / H2H"
    )
