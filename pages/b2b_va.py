import streamlit as st
from components.section_sidebar import render_section_sidebar

st.set_page_config(layout="wide")

center, right = st.columns([4.5, 1.5])

# RIGHT: SECTION SIDEBAR
with right:
    render_section_sidebar([
        "Overview",
        "Use case",
        "Integration Methods"
    ])

# CENTER CONTENT
with center:
    st.markdown("**B2B > Virtual Account**")
    st.title("Virtual Account")

    st.markdown('<a name="overview"></a>', unsafe_allow_html=True)
    st.header("Overview")
    st.write("VA allows merchants to collect payments via unique accounts.")

    st.markdown('<a name="use-case"></a>', unsafe_allow_html=True)
    st.header("Use case")
    st.write("Direct Merchant and Master Merchant models.")

    st.markdown('<a name="integration-methods"></a>', unsafe_allow_html=True)
    st.header("Integration Methods")

    st.subheader("Direct Merchant")
    st.page_link(
        "pages/b2b_va_direct_basic.py",
        label="Direct MRC / Basic"
    )
    st.page_link(
        "pages/b2b_va_direct_h2h.py",
        label="Direct MRC / H2H"
    )
