import streamlit as st
import json

def render_b2b_va():

    st.markdown("<div id='overview'></div>", unsafe_allow_html=True)
    st.title("B2B / Virtual Account (VA)")

    st.write("""
Virtual Account (VA) allows merchants to generate unique bank account numbers
to collect payments from customers.
""")

    st.divider()

    st.markdown("<div id='usecase'></div>", unsafe_allow_html=True)
    st.header("Use case")

    st.subheader("Direct Merchant")
    st.write("""
You operate as a single merchant and collect payments directly from customers.

Recommended integration:
- Basic Integration
- Pro Integration
""")

    st.subheader("Master Merchant")
    st.write("""
You operate a platform or marketplace and collect payments on behalf of sub-merchants.

Recommended integration:
- Pro Integration
- Host-to-Host Integration
""")

    st.divider()

    st.markdown("<div id='integrate'></div>", unsafe_allow_html=True)
    st.header("Integrate Methods")

    st.subheader("Basic Integration")
    st.write("Redirect or SDK-based integration for quick onboarding.")

    st.subheader("Pro Integration")
    st.write("Full API integration with custom checkout experience.")

    st.subheader("Host-to-Host Integration")
    st.write("Server-to-server integration for enterprise platforms.")

    st.divider()

    st.markdown("<div id='sandbox'></div>", unsafe_allow_html=True)
    st.header("Sandbox")

    st.code("https://sandbox-api.company.com/va")

    st.table([
        {"Method": "POST", "Endpoint": "/v1/virtual-accounts", "Description": "Create VA"},
        {"Method": "GET", "Endpoint": "/v1/virtual-accounts/{vaId}", "Description": "Get VA info"}
    ])

    st.code(json.dumps({
        "requestId": "req-123",
        "merchantId": "MERCHANT_001",
        "amount": 100000,
        "currency": "VND"
    }, indent=2))

    st.divider()

    st.markdown("<div id='api'></div>", unsafe_allow_html=True)
    st.header("API Reference")

    st.subheader("Create Virtual Account")
    st.code("POST /v1/virtual-accounts")

    st.table([
        {"Field": "merchantId", "Type": "string", "Required": "Yes"},
        {"Field": "amount", "Type": "number", "Required": "Yes"},
        {"Field": "currency", "Type": "string", "Required": "Yes"}
    ])

    st.divider()

    st.markdown("<div id='security'></div>", unsafe_allow_html=True)
    st.header("Security")

    st.write("""
All requests must be signed using HMAC SHA256.
Required headers:
- X-Request-Id
- X-Timestamp
- X-Client-Id
- X-Signature
""")

    st.divider()

    st.markdown("<div id='webhook'></div>", unsafe_allow_html=True)
    st.header("Webhook")

    st.code("POST https://merchant.com/webhook/va")

    st.divider()

    st.markdown("<div id='errors'></div>", unsafe_allow_html=True)
    st.header("Error Codes")

    st.table([
        {"Code": "INVALID_SIGNATURE", "Message": "Signature verification failed"},
        {"Code": "VA_NOT_FOUND", "Message": "Virtual account not found"},
        {"Code": "EXPIRED_VA", "Message": "Virtual account expired"}
    ])

    st.success("Mock content – demo purpose only")
