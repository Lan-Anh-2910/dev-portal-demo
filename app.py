import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dev Portal Demo", layout="wide")

# ---------- DATA ----------
NAV = {
    "B2B": {
        "VA": ["Overview", "Use case", "Sandbox", "API Reference"],
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
    },
    "Cross-border": {
        "Collection": ["Overview", "Flow", "Sandbox", "API Reference"],
        "Disbursement": ["Overview", "Flow", "Sandbox", "API Reference"],
        "Check transaction status": ["Overview", "API Reference"],
        "Check balance": ["Overview", "API Reference"],
        "Payment": ["Overview", "API Reference"],
        "Refund": ["Overview", "API Reference"],
        "Settlement": ["Overview", "API Reference"],
        "Onboarding sellers": ["Overview", "API Reference"]
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
left, center, right = st.columns([1.8, 4.4, 1.8])

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

            label = f"👉 {sp}" if is_active else f"&nbsp;&nbsp;{sp}"

            if st.markdown(
                f"<div style='cursor:pointer; color:{'#1f77b4' if is_active else '#444'}'>{label}</div>",
                unsafe_allow_html=True
            ):
                pass

            if st.button(
                sp,
                key=f"{product}_{sp}",
                help=sp,
                use_container_width=True
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

    if st.session_state.section == "Overview":
        st.markdown("""
        Đây là **Overview**.

        Nội dung demo cho API documentation portal.
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
        st.info("Nội dung đang được cập nhật.")
