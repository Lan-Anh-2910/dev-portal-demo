import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dev Portal Demo", layout="wide")

# ---------- SECTION TEMPLATES ----------
B2B_SECTIONS = [
    "Overview",
    "Use case",
    "Integrate Methods",
    "Sandbox",
    "API Reference",
    "Security",
    "Webhook",
    "Error Codes"
]

CROSS_BORDER_SECTIONS = [
    "Overview",
    "Flow",
    "Sandbox",
    "API Reference",
    "Security",
    "Webhook",
    "Error Codes"
]

# ---------- NAV STRUCTURE ----------
NAV = {
    "B2B": {
        "VA": B2B_SECTIONS,
        "BNPL": B2B_SECTIONS,
        "Installment": B2B_SECTIONS,
        "Card Payment": B2B_SECTIONS,
    },
    "Bill": {
        "Bill Payment": B2B_SECTIONS,
        "Insurance": B2B_SECTIONS,
    },
    "Leadgen": {
        "Leadgen": ["Overview"]
    },
    "Cross-border": {
        "Collection": CROSS_BORDER_SECTIONS,
        "Disbursement": CROSS_BORDER_SECTIONS,
        "Check transaction status": CROSS_BORDER_SECTIONS,
        "Check balance": CROSS_BORDER_SECTIONS,
        "Payment": CROSS_BORDER_SECTIONS,
        "Refund": CROSS_BORDER_SECTIONS,
        "Settlement": CROSS_BORDER_SECTIONS,
        "Onboarding sellers": CROSS_BORDER_SECTIONS,
    }
}

# ---------- SESSION STATE ----------
if "product" not in st.session_state:
    st.session_state.product = "B2B"

if "subproduct" not in st.session_state:
    st.session_state.subproduct = "VA"

if "section" not in st.session_state:
    st.session_state.section = "Overview"

# ---------- LAYOUT ----------
left, center, right = st.columns([1.9, 4.2, 1.9])

# ---------- LEFT: PRODUCT + SUBPRODUCT ----------
with left:
    st.markdown("### Products")

    for product, subs in NAV.items():
        st.markdown(f"**{product}**")

        for sp in subs.keys():
            is_active = (
                st.session_state.product == product
                and st.session_state.subproduct == sp
            )

            if st.button(
                sp,
                key=f"{product}_{sp}",
                use_container_width=True,
                type="primary" if is_active else "secondary"
            ):
                st.session_state.product = product
                st.session_state.subproduct = sp
                st.session_state.section = NAV[product][sp][0]
                st.rerun()

        st.markdown("---")

# ---------- RIGHT: SECTIONS ----------
with right:
    st.markdown("### Sections")

    sections = NAV[st.session_state.product][st.session_state.subproduct]

    for sec in sections:
        is_active = st.session_state.section == sec

        if st.button(
            sec,
            key=f"sec_{sec}",
            use_container_width=True,
            type="primary" if is_active else "secondary"
        ):
            st.session_state.section = sec
            st.rerun()

# ---------- CENTER: CONTENT ----------
with center:
    st.markdown(
        f"##### {st.session_state.product} / {st.session_state.subproduct}"
    )
    st.title(st.session_state.section)
    st.divider()

    # -------- CONTENT MOCK --------
    if st.session_state.section == "Overview":
        st.markdown("""
        Đây là **Overview**.

        Nội dung mô tả tổng quan API, phạm vi sử dụng,
        đối tượng tích hợp và luồng chính.
        """)

    elif st.session_state.section == "Flow":
        st.markdown("""
        ### Flow Diagram
        1. Client gửi request
        2. System validate
        3. Process & response
        """)

    elif st.session_state.section == "API Reference":
        st.subheader("POST /api/v1/example")

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
            "data": {"id": "demo_001"}
        })

    else:
        st.info("Nội dung demo – sẽ cập nhật sau.")
