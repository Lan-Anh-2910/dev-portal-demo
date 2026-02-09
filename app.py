import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dev Portal",
    layout="wide"
)

# ---------- DATA STRUCTURE ----------
NAV = {
    "Cross-border": {
        "Collection": [
            "Overview", "Flow", "Sandbox",
            "API Reference", "Webhook", "Security", "Error Codes"
        ],
        "Disbursement": [
            "Overview", "Flow", "Sandbox",
            "API Reference", "Webhook", "Security", "Error Codes"
        ]
    },
    "B2B": {
        "VA": [
            "Overview", "Use case", "Integrate Methods",
            "Sandbox", "API Reference", "Webhook", "Error Codes"
        ],
        "BNPL": ["Overview", "API Reference"],
        "Installment": ["Overview", "API Reference"],
        "Card Payment": ["Overview", "API Reference"]
    },
    "Bill": {
        "Bill Payment": ["Overview", "API Reference"],
        "Insurance": ["Overview", "API Reference"]
    },
    "Leadgen": {
        "Overview": ["Overview"]
    }
}

# ---------- SIDEBAR ----------
st.sidebar.title("📘 Dev Portal")

product = st.sidebar.selectbox(
    "Product",
    list(NAV.keys())
)

module = st.sidebar.selectbox(
    "Module",
    list(NAV[product].keys())
)

section = st.sidebar.radio(
    "Documentation",
    NAV[product][module]
)

# ---------- MAIN CONTENT ----------
st.markdown(f"### {product}")
st.title(module)
st.caption(section)

st.divider()

# ---------- CONTENT RENDER ----------
if section == "Overview":
    st.markdown("""
    Welcome to the **Overview** section.

    Đây là nội dung demo cho module này.
    Có thể mô tả mục đích, phạm vi, và cách sử dụng tổng quan.
    """)

elif section == "API Reference":
    st.subheader("POST /api/v1/example")

    st.markdown("**Description**")
    st.write("This API endpoint is used for demonstration purposes.")

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

else:
    st.info("Content will be updated later.")
