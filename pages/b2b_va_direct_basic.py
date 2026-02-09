import streamlit as st

st.set_page_config(page_title="VA - Direct Merchant - Basic", layout="wide")

# ===== Breadcrumb =====
st.markdown(
    """
**[B2B](app.py) > [Virtual Account](pages/b2b_va.py) > Direct Merchant > Basic Integration**
""",
    unsafe_allow_html=True
)

st.title("VA – Direct Merchant – Basic Integration")

# ===== CTA LINKS =====
st.info("Explore other VA integrations:")

col1, col2, col3 = st.columns(3)

with col1:
    st.page_link(
        "pages/b2b_va_direct_h2h.py",
        label="Direct Merchant / Host-to-Host"
    )

with col2:
    st.page_link(
        "pages/b2b_va_master_basic.py",
        label="Master Merchant / Basic"
    )

with col3:
    st.page_link(
        "pages/b2b_va_master_h2h.py",
        label="Master Merchant / Host-to-Host"
    )

# ===== Overview =====
st.header("Overview")
st.write("""
This integration is designed for Direct Merchants who want a simple and quick
way to create and manage Virtual Accounts.
""")

# ===== Flow =====
st.header("Flow")
st.write("""
1. Create Virtual Account  
2. Customer transfers funds  
3. System receives payment notification  
""")

# ===== Sandbox =====
st.header("Sandbox")

st.write("**Base URL**")
st.code("https://sandbox-api.example.com")

st.write("**Sample Credentials**")
st.code("""
client_id: sandbox_client_id
api_key: sandbox_api_key
""")

st.write("**Available APIs**")
st.table({
    "Method": ["POST", "GET"],
    "Endpoint": [
        "/v1/virtual-accounts",
        "/v1/virtual-accounts/{va_id}"
    ],
    "Description": [
        "Create virtual account",
        "Get virtual account detail"
    ]
})

# ===== API Reference =====
st.header("API Reference")

st.subheader("Create Virtual Account")

st.code("""
POST /v1/virtual-accounts

Headers:
Authorization: Bearer <api_key>

Request body:
{
  "requestId": "123456",
  "amount": 100000,
  "currency": "VND"
}
""", language="json")

st.code("""
Response:
{
  "vaId": "VA123",
  "status": "ACTIVE"
}
""", language="json")

# ===== Security =====
st.header("Security")
st.write("""
All requests must be signed using API Key and Request ID.
""")

# ===== Webhook =====
st.header("Webhook")
st.write("""
Webhook will be sent when payment is completed.
""")

st.code("""
POST /webhook/va/payment
""")

# ===== Error Codes =====
st.header("Error Codes")

st.table({
    "Code": ["400", "401", "500"],
    "Message": [
        "Invalid request",
        "Unauthorized",
        "Internal server error"
    ]
})
