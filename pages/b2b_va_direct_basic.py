import streamlit as st
from components.section_sidebar import render_section_sidebar

st.set_page_config(layout="wide")

center, right = st.columns([4.5, 1.5])

# RIGHT: SECTION SIDEBAR
with right:
    render_section_sidebar([
        "Overview",
        "Flow",
        "Sandbox",
        "API Reference",
        "Security",
        "Webhook",
        "Error Codes"
    ])

# CENTER CONTENT
with center:
    st.markdown("**B2B > VA > Direct Merchant > Basic**")
    st.title("VA – Direct Merchant – Basic")

    st.markdown('<a name="overview"></a>', unsafe_allow_html=True)
    st.header("Overview")
    st.write("Basic integration for Direct Merchant.")

    st.markdown('<a name="flow"></a>', unsafe_allow_html=True)
    st.header("Flow")
    st.write("Create VA → Pay → Webhook")

    st.markdown('<a name="sandbox"></a>', unsafe_allow_html=True)
    st.header("Sandbox")
    st.code("https://sandbox-api.example.com")

    st.markdown('<a name="api-reference"></a>', unsafe_allow_html=True)
    st.header("API Reference")
    st.code("POST /v1/virtual-accounts")

    st.markdown('<a name="security"></a>', unsafe_allow_html=True)
    st.header("Security")
    st.write("API Key authentication")

    st.markdown('<a name="webhook"></a>', unsafe_allow_html=True)
    st.header("Webhook")
    st.code("POST /webhook/va")

    st.markdown('<a name="error-codes"></a>', unsafe_allow_html=True)
    st.header("Error Codes")
    st.table({
        "Code": ["400", "401", "500"],
        "Message": ["Bad request", "Unauthorized", "Server error"]
    })
