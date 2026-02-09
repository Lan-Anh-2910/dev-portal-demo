import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dev Portal Demo", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
.nav-product {
    font-weight: 600;
    margin-top: 12px;
    color: #333;
}
.nav-sub {
    padding: 6px 10px;
    margin-left: 22px;
    border-radius: 6px;
    cursor: pointer;
    color: #555;
}
.nav-sub:hover {
    background-color: #f5f5f5;
}
.nav-sub.active {
    background-color: #fde7f3;
    color: #d63384;
    font-weight: 600;
}
.toggle {
    cursor: pointer;
    color: #888;
    margin-right: 6px;
}
</style>
""", unsafe_allow_html=True)

# ---------- SECTION TEMPLATES ----------
B2B_SECTIONS = [
    "Overview", "Use case", "Integrate Methods",
    "Sandbox", "API Reference", "Security",
    "Webhook", "Error Codes"
]

CROSS_BORDER_SECTIONS = [
    "Overview", "Flow", "Sandbox",
    "API Reference", "Security",
    "Webhook", "Error Codes"
]

# ---------- NAV ----------
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

# product open state
for product in NAV.keys():
    key = f"open_{product}"
    if key not in st.session_state:
        st.session_state[key] = False

# ---------- LAYOUT ----------
left, center, right = st.columns([2, 4, 2])

# ---------- LEFT: PRODUCT COLLAPSE ----------
with left:
    st.markdown("### Overview")

    for product, subs in NAV.items():
        open_key = f"open_{product}"
        icon = "▼" if st.session_state[open_key] else "▶"

        cols = st.columns([0.15, 0.85])
        with cols[0]:
            if st.button(icon, key=f"toggle_{product}"):
                st.session_state[open_key] = not st.session_state[open_key]
                st.rerun()

        with cols[1]:
            st.markdown(
                f"<div class='nav-product'>{product}</div>",
                unsafe_allow_html=True
            )

        # show subproducts ONLY when open
        if st.session_state[open_key]:
            for sp in subs.keys():
                is_active = (
                    st.session_state.product == product
                    and st.session_state.subproduct == sp
                )

                css = "nav-sub active" if is_active else "nav-sub"

                if st.button(
                    sp,
                    key=f"sub_{product}_{sp}",
                    use_container_width=True
                ):
                    st.session_state.product = product
                    st.session_state.subproduct = sp
                    st.session_state.section = NAV[product][sp][0]
                    st.rerun()

# ---------- RIGHT: SECTIONS ----------
with right:
    st.markdown("### Sections")

    sections = NAV[st.session_state.product][st.session_state.subproduct]

    for sec in sections:
        anchor = sec.lower().replace(" ", "-")
        st.markdown(f"- [{sec}](#{anchor})")

# ---------- CENTER: FAKE CONTENT ----------
with center:
    st.markdown(
        f"##### {st.session_state.product} / {st.session_state.subproduct}"
    )

    sections = NAV[st.session_state.product][st.session_state.subproduct]

    for sec in sections:
        anchor = sec.lower().replace(" ", "-")

        # Anchor
        st.markdown(f"<div id='{anchor}'></div>", unsafe_allow_html=True)

        # Title
        st.markdown(f"## {sec}")
        st.divider()

        # -------- FAKE CONTENT --------
        st.markdown(f"""
**Description**  
This is mock content for **{sec}** under **{st.session_state.subproduct}**.

**What you can do**
- Understand feature behavior
- Review integration approach
- Explore API structure
- Test in sandbox environment

**Notes**
All information here is fake and for demo purposes only.
""")

        # API Reference mock
        if sec == "API Reference":
            st.subheader("POST /api/v1/demo")

            st.markdown("**Headers**")
            st.code("""
Authorization: Bearer {API_KEY}
Content-Type: application/json
""")

            st.markdown("**Request Body**")
            st.json({
                "amount": 100000,
                "currency": "VND",
                "order_id": "ORDER_123"
            })

            st.markdown("**Response Example**")
            st.json({
                "status": "success",
                "transaction_id": "TXN_456"
            })

