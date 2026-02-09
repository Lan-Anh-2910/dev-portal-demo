import streamlit as st

def anchor(id):
    st.markdown(f"<a id='{id}'></a>", unsafe_allow_html=True)

def scroll_button(label, anchor_id):
    st.markdown(
        f"""
        <a href="#{anchor_id}">
            <button style="margin:4px 0">{label}</button>
        </a>
        """,
        unsafe_allow_html=True
    )

def render():
    col_left, col_main, col_right = st.columns([2, 6, 2])

    # ========== RIGHT NAV ==========
    with col_right:
        st.markdown("### Sections")
        st.markdown("""
        - Overview
        - Use case
        - Integrate Methods
        - Sandbox
        - API Reference
        - Security
        - Webhook
        - Error Codes
        """)

    # ========== MAIN CONTENT ==========
    with col_main:
        anchor("overview")
        st.header("VA – Virtual Account")
        st.write("Virtual Account enables merchants to receive payments via dedicated accounts.")

        anchor("use-case")
        st.header("Use case")

        st.subheader("Direct Merchant")
        st.write("You collect payments directly from end users.")

        scroll_button("Basic Integration", "basic")
        scroll_button("Host-to-Host Integration", "h2h")

        st.subheader("Master Merchant")
        st.write("You manage sub-merchants and collect on their behalf.")

        scroll_button("Basic Integration", "basic")
        scroll_button("Host-to-Host Integration", "h2h")

        # ========== INTEGRATION METHODS ==========
        anchor("integrate")
        st.header("Integrate Methods")

        anchor("basic")
        st.subheader("Basic Integration")
        st.write("Simple integration using REST APIs.")

        st.markdown("**Supported use cases:** Direct, Master")

        anchor("sandbox")
        st.header("Sandbox")
        st.table({
            "Endpoint": ["/sandbox/va"],
            "Method": ["POST"],
            "Description": ["Create virtual account"]
        })

        anchor("api")
        st.header("API Reference")
        st.code("""
POST /va/create
{
  "amount": 100000,
  "currency": "VND"
}
        """)

        anchor("security")
        st.header("Security")
        st.write("OAuth2, IP Whitelist")

        anchor("webhook")
        st.header("Webhook")
        st.code("""
POST /webhook/va/payment
        """)

        anchor("error")
        st.header("Error Codes")
        st.table({
            "Code": ["VA_001", "VA_002"],
            "Message": ["Invalid amount", "Account not found"]
        })

        # ========== HOST TO HOST ==========
        anchor("h2h")
        st.subheader("Host-to-Host Integration")
        st.write("Advanced integration with direct system connection.")
