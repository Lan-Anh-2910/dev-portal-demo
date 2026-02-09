import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dev Portal Demo", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
.nav-title {
    margin-top: 14px;
    font-weight: 600;
    color: #333;
}
.nav-item {
    padding: 6px 10px;
    margin-left: 18px;
    border-radius: 6px;
    cursor: pointer;
    color: #555;
}
.nav-item:hover {
    background-color: #f5f5f5;
}
.nav-item.active {
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
    "Sandbox", "API Reference", "Security", "Webhook", "Error Codes"
]

CROSS_BORDER_SECTIONS = [
    "Overview", "Flow", "Sandbox",
    "API Reference", "Security", "Webhook", "Error Codes"
]

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

# collapse state
for p, subs in NAV.items():
    for sp in subs:
        key = f"open_{p}_{sp}"
        if key not in st.session_state:
            st.session_state[key] = False

# ---------- LAYOUT ----------
left, center, right = st.columns([2, 4, 2])

# ---------- LEFT: COLLAPSIBLE MENU ----------
with left:
    st.markdown("### Overview")

    for product, subs in NAV.items():
        st.markdown(f"<div class='nav-title'>{product}</div>", unsafe_allow_html=True)

        for sp in subs.keys():
            open_key = f"open_{product}_{sp}"
            is_active = (
                st.session_state.product == product
                and st.session_state.subproduct == sp
            )

            icon = "▼" if st.session_state[open_key] else "▶"

            cols = st.columns([0.15, 0.85])
            with cols[0]:
                if st.button(icon, key=f"toggle_{product}_{sp}"):
                    st.session_state[open_key] = not st.session_state[open_key]
                    st.rerun()

            with cols[1]:
                css = "nav-item active" if is_active else "nav-item"
                if st.button(sp, key=f"nav_{product}_{sp}", use_container_width=True):
                    st.session_state.product = product
                    st.session_state.subproduct = sp
                    st.session_state.section = NAV[product][sp][0]
                    st.session_state[open_key] = True
                    st.rerun()

# ---------- RIGHT: SECTIONS ----------
with right:
    st.markdown("### Sections")
    for sec in NAV[st.session_state.product][st.session_state.subproduct]:
        if st.button(sec, key=f"sec_{sec}", use_container_width=True):
            st.session_state.section = sec
            st.rerun()

# ---------- CENTER: FAKE CONTENT ----------
with center:
    st.markdown(
        f"##### {st.session_state.product} / {st.session_state.subproduct}"
    )
    st.title(st.session_state.section)
    st.divider()

    # ---- FAKE CONTENT ----
    st.markdown(f"""
### {st.session_state.section}

This is **mock content** for demo purposes.

**Description**
This section describes how the `{st.session_state.subproduct}` feature works in the `{st.session_state.product}` product.

**Key Points**
- Simple integration
- Secure authentication
- Scalable architecture
- Suitable for sandbox and production

**Notes**
All data shown here is fake and used only to demonstrate UI and structure.
""")

    if st.session_state.section == "API Reference":
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
