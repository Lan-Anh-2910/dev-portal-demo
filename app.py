import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dev Portal Demo", layout="wide")

# ---------- DATA ----------
PRODUCTS = {
    "Cross-border": [
        "Overview", "Flow", "Sandbox",
        "API Reference", "Webhook", "Security", "Error Codes"
    ],
    "B2B": [
        "Overview", "Use case", "Integrate Methods",
        "Sandbox", "API Reference", "Webhook", "Error Codes"
    ],
    "Bill": [
        "Overview", "API Reference"
    ],
    "Leadgen": [
        "Overview"
    ]
}

# ---------- SESSION STATE ----------
if "product" not in st.session_state:
    st.session_state.product = "Cross-border"

if "section" not in st.session_state:
    st.session_state.section = "Overview"

# ---------- LAYOUT ----------
left, center, right = st.columns([1.2, 3.6, 1.6])

# ---------- LEFT: PRODUCTS ----------
with left:
    st.markdown("### Products")
    for p in PRODUCTS.keys():
        if st.button(
            p,
            use_container_width=True,
            type="primary" if st.session_state.product == p else "secondary"
        ):
            st.session_state.product = p
            st.session_state.section = PRODUCTS[p][0]

# ---------- RIGHT: SUBNAMES ----------
with right:
    st.markdown("### Sections")
    for s in PRODUCTS[st.session_state.product]:
        if st.button(
            s,
            use_container_width=True,
            type="primary" if st.session_state.section == s else "secondary"
        ):
            st.session_state.section = s

# ---------- CENTER: CONTENT ----------
with center:
    st.markdown(f"##### {st.session_state.product}")
    st.title(st.session_state.section)
    st.divider()

    # ---- CONTENT TEMPLATE ----
    if st.session_state.section == "Overview":
        st.markdown("""
        Đây là **Overview** của product.

        Nội dung demo, mô tả tổng quan, phạm vi sử dụng,
        và các thông tin cần biết trước khi tích hợp.
        """)

    elif st.session_state.section == "API Reference":
        st.subheader("POST /api/v1/example")

        st.markdown("**Description**")
        st.write("API endpoint dùng cho demo Dev Portal.")

        st.markdown("**Headers**")
        st.code("""
Authorization: Bearer {API_KEY}
Content-Type: application/json
""")

        st.markdown("**Request Parameters**")
        df = pd.DataFrame({
            "Field": ["amount", "currency"],
            "Type": ["number", "string"],
            "Required": ["Yes", "Yes"]
        })
        st.table(df)

        st.markdown("**Example Response**")
        st.json({
            "status": "success",
            "data": {
                "transaction_id": "demo_123"
            }
        })

    else:
        st.info("Nội dung đang được cập nhật.")
