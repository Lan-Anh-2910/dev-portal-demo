import streamlit as st
import json

st.set_page_config(
    page_title="Dev Portal – B2B VA",
    layout="wide"
)

# =========================
# CSS
# =========================
st.markdown("""
<style>
:target { scroll-margin-top: 80px; }

.section {
    padding-top: 20px;
    padding-bottom: 40px;
}

.code-box {
    background: #0f172a;
    color: #e5e7eb;
    padding: 16px;
    border-radius: 8px;
    font-size: 13px;
}

.table th {
    background-color: #f3f4f6;
}
</style>
""", unsafe_allow_html=True)

# =========================
# LAYOUT
# =========================
left, center, right = st.columns([1.2, 4.5, 1.6])

# =========================
# LEFT NAV
# =========================
with left:
    st.markdown("### Products")

    with st.expander("B2B", expanded=True):
        st.markdown("**VA**")
        st.markdown("- BNPL")
        st.markdown("- Installment")
        st.markdown("- Card Payment")

    with st.expander("Bill"):
        st.markdown("- Bill Payment")
        st.markdown("- Insurance")

# =========================
# RIGHT NAV
# =========================
with right:
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

# =========================
# CENTER CONTENT
# =========================
with center:

    # OVERVIEW
    st.markdown("<div id='overview' class='section'></div>", unsafe_allow_html=True)
    st.header("Overview")
    st.write("""
Virtual Account (VA) enables merchants to generate unique bank account
numbers for collecting payments from customers.
""")

    # USE CASE
    st.markdown("<div id='usecase' class='section'></div>", unsafe_allow_html=True)
    st.header("Use case")

    st.subheader("Direct Merchant")
    st.write("""
You operate as a single merchant and collect payments directly from customers.

**Recommended integration**
- Basic Integration
- Pro Integration
""")

    st.subheader("Master Merchant")
    st.write("""
You operate a platform or marketplace and collect payments on behalf of sub-merchants.

**Recommended integration**
- Pro Integration
- Host-to-Host Integration
""")

    # INTEGRATE METHODS
    st.markdown("<div id='integrate' class='section'></div>", unsafe_allow_html=True)
    st.header("Integrate Methods")

    st.subheader("Basic Integration")
    st.write("Redirect or SDK based integration for fast onboarding.")

    st.subheader("Pro Integration")
    st.write("Full API integration with custom payment flow.")

    st.subheader("Host-to-Host")
    st.write("Server-to-server integration for enterprise platforms.")

    # SANDBOX
    st.markdown("<div id='sandbox' class='section'></div>", unsafe_allow_html=True)
    st.header("Sandbox")

    st.markdown("**Base URL**")
    st.code("https://sandbox-api.company.com/va")

    st.markdown("**Available APIs**")
    st.table([
        {"Method": "POST", "Endpoint": "/v1/virtual-accounts", "Description": "Create VA"},
        {"Method": "GET", "Endpoint": "/v1/virtual-accounts/{vaId}", "Description": "Get VA info"}
    ])

    st.markdown("**Sample Request**")
    st.code(json.dumps({
        "requestId": "abc-123",
        "merchantId": "MERCHANT_001",
        "amount": 100000,
        "currency": "VND"
    }, indent=2))

    st.markdown("**Sample Response**")
    st.code(json.dumps({
        "code": "SUCCESS",
        "message": "Success",
        "data": {
            "vaId": "VA123456",
            "accountNumber": "123456789",
            "status": "ACTIVE"
        }
    }, indent=2))

    # API REFERENCE
    st.markdown("<div id='api' class='section'></div>", unsafe_allow_html=True)
    st.header("API Reference")

    st.subheader("Create Virtual Account")
    st.code("POST /v1/virtual-accounts")

    st.table([
        {"Field": "merchantId", "Type": "string", "Required": "Yes"},
        {"Field": "amount", "Type": "number", "Required": "Yes"},
        {"Field": "currency", "Type": "string", "Required": "Yes"}
    ])

    st.subheader("Get Virtual Account")
    st.code("GET /v1/virtual-accounts/{vaId}")

    # SECURITY
    st.markdown("<div id='security' class='section'></div>", unsafe_allow_html=True)
    st.header("Security")

    st.write("""
All requests must be signed using HMAC SHA256.
IP whitelisting is required for Host-to-Host integration.
""")

    # WEBHOOK
    st.markdown("<div id='webhook' class='section'></div>", unsafe_allow_html=True)
    st.header("Webhook")

    st.code("POST https://merchant.com/webhook/va")

    st.write("Triggered when VA is paid or expired.")

    # ERROR CODES
    st.markdown("<div id='errors' class='section'></div>", unsafe_allow_html=True)
    st.header("Error Codes")

    st.table([
        {"Code": "INVALID_SIGNATURE", "Message": "Signature verification failed"},
        {"Code": "VA_NOT_FOUND", "Message": "Virtual account not found"},
        {"Code": "EXPIRED_VA", "Message": "Virtual account expired"}
    ])

    st.success("Mock content – for demo purpose only")
