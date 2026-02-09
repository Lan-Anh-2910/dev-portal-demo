import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dev Portal",
    layout="wide"
)

# ---------- SIDEBAR (LEFT) ----------
st.sidebar.title("📘 Dev Portal")

product = st.sidebar.selectbox(
    "Product",
    ["Cross-border", "B2B", "Bill", "Leadgen"]
)

module_map = {
    "Cross-border": ["Collection", "Disbursement"],
    "B2B": ["VA", "BNPL", "Installment", "Card Payment"],
    "Bill": ["Bill Payment", "Insurance"],
    "Leadgen": ["Overview"]
}

module = st.sidebar.selectbox(
    "Module",
    module_map[product]
)

# ---------- MAIN HEADER ----------
st.markdown(f"### {product}")
st.title(module)

st.divider()

# ---------- SUB TABS (RIGHT / TOP) ----------
tabs = st.tabs([
    "Overview",
    "Flow",
    "Sandbox",
    "API Reference",
    "Webhook",
    "Security",
    "Error Codes"
])

# ---------- TAB CONTENT ----------
with tabs[0]:
    st.subheader("Overview")
    st.markdown("""
    Đây là phần mô tả tổng quan module.

    Nội dung demo – sẽ cập nhật sau.
    """)

with tabs[1]:
    st.subheader("Flow")
    st.info("Flow diagram sẽ được thêm sau.")

with tabs[2]:
    st.subheader("Sandbox")
    st.markdown("""
    Base URL (Sandbox):

    ```
    https://sandbox.api.company.com
    ```
    """)

with tabs[3]:
    st.subheader("POST /api/v1/example")

    st.markdown("**Description**")
    st.write("API dùng cho mục đích demo.")

    st.markdown("**Headers**")
    st.code("""
Authorization: Bearer {API_KEY}
Content-Type: application/json
""")

    st.markdown("**Request Parameters**")
    df = pd.DataFrame({
        "Field": ["amount", "currency"],
        "Type": ["number", "string"],
        "Required": ["Yes", "Yes"],
        "Description": ["Transaction amount", "Currency code"]
    })
    st.table(df)

    st.markdown("**Example Response**")
    st.json({
        "status": "success",
        "data": {
            "transaction_id": "abc123"
        }
    })

with tabs[4]:
    st.subheader("Webhook")
    st.info("Webhook documentation placeholder.")

with tabs[5]:
    st.subheader("Security")
    st.markdown("Authentication, signature, IP whitelist...")

with tabs[6]:
    st.subheader("Error Codes")
    st.table(pd.DataFrame({
        "Code": ["400", "401", "500"],
        "Description": [
            "Bad Request",
            "Unauthorized",
            "Internal Server Error"
        ]
    }))
