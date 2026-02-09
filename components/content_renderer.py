import streamlit as st
from components.section_sidebar import render_section_sidebar

def render_content(route):
    center, right = st.columns([4.5, 1.5])

    # HOME
    if route == "home":
        with center:
            st.title("Developer Portal")
            st.write("Choose a product on the left")

    # ===== VA OVERVIEW PAGE =====
    elif route == "b2b_va":
        with right:
            render_section_sidebar([
                "Overview",
                "Use case",
                "Integration Methods"
            ])

        with center:
            st.title("B2B / Virtual Account")

            # ===== Overview =====
            st.markdown('<a id="overview"></a>', unsafe_allow_html=True)
            st.header("Overview")
            st.write("Virtual Account allows merchants to receive payments via unique virtual accounts.")

            # ===== Use case =====
            st.markdown('<a id="use-case"></a>', unsafe_allow_html=True)
            st.header("Use case")

            st.subheader("Direct Merchant")
            st.write("You integrate directly with our VA system.")

            if st.button("Direct Merchant - Basic"):
                st.session_state.route = "b2b_va_direct_basic"

            if st.button("Direct Merchant - H2H"):
                st.session_state.route = "b2b_va_direct_h2h"

            st.subheader("Master Merchant")
            st.write("You manage sub-merchants under your system.")

            if st.button("Master Merchant - Basic"):
                st.session_state.route = "b2b_va_master_basic"

            if st.button("Master Merchant - H2H"):
                st.session_state.route = "b2b_va_master_h2h"

            # ===== Integration Methods =====
            st.markdown('<a id="integration-methods"></a>', unsafe_allow_html=True)
            st.header("Integration Methods")
            st.write("Choose an integration method based on your use case.")

    # ===== DIRECT / BASIC =====
    elif route == "b2b_va_direct_basic":
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

        with center:
            st.markdown("B2B > VA > Direct Merchant > Basic")
            st.title("Direct Merchant - Basic Integration")

            st.markdown('<a id="overview"></a>', unsafe_allow_html=True)
            st.header("Overview")
            st.write("Basic integration for Direct Merchants.")

            st.markdown('<a id="flow"></a>', unsafe_allow_html=True)
            st.header("Flow")
            st.write("1. Create VA → 2. Customer pays → 3. Callback")

            st.markdown('<a id="sandbox"></a>', unsafe_allow_html=True)
            st.header("Sandbox")
            st.table({
                "Field": ["accountNo", "amount"],
                "Example": ["123456", "100000"]
            })

            st.markdown('<a id="api-reference"></a>', unsafe_allow_html=True)
            st.header("API Reference")
            st.code("POST /v1/va/create")

            st.markdown('<a id="security"></a>', unsafe_allow_html=True)
            st.header("Security")
            st.write("HMAC SHA256 signature")

            st.markdown('<a id="webhook"></a>', unsafe_allow_html=True)
            st.header("Webhook")
            st.write("POST /webhook/va/payment")

            st.markdown('<a id="error-codes"></a>', unsafe_allow_html=True)
            st.header("Error Codes")
            st.write("VA_001: Invalid amount")

    # ===== DIRECT / H2H =====
    elif route == "b2b_va_direct_h2h":
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

        with center:
            st.markdown("B2B > VA > Direct Merchant > H2H")
            st.title("Direct Merchant - Host to Host")

            st.markdown('<a id="overview"></a>', unsafe_allow_html=True)
            st.header("Overview")
            st.write("H2H integration for high volume merchants.")

            st.markdown('<a id="flow"></a>', unsafe_allow_html=True)
            st.header("Flow")
            st.write("Dedicated connection between systems.")

            st.markdown('<a id="sandbox"></a>', unsafe_allow_html=True)
            st.header("Sandbox")
            st.code("GET /v1/va/status")

            st.markdown('<a id="api-reference"></a>', unsafe_allow_html=True)
            st.header("API Reference")
            st.code("POST /v1/va/h2h/create")

            st.markdown('<a id="security"></a>', unsafe_allow_html=True)
            st.header("Security")
            st.write("Mutual TLS")

            st.markdown('<a id="webhook"></a>', unsafe_allow_html=True)
            st.header("Webhook")
            st.write("Optional")

            st.markdown('<a id="error-codes"></a>', unsafe_allow_html=True)
            st.header("Error Codes")
            st.write("H2H_001: Connection timeout")
