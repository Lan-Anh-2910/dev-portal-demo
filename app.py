import streamlit as st
import pandas as pd

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(page_title="Dev Portal Demo", layout="wide")

# =========================================================
# GLOBAL CSS
# =========================================================
st.markdown("""
<style>

/* ---------- Sticky left & right ---------- */
div[data-testid="column"]:nth-child(1),
div[data-testid="column"]:nth-child(3) {
    position: sticky;
    top: 80px;
    height: calc(100vh - 80px);
    overflow-y: auto;
}

/* ---------- Sidebar styles ---------- */
.nav-product {
    font-weight: 600;
    margin-top: 14px;
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

/* ---------- Section anchor ---------- */
:target {
    scroll-margin-top: 90px;
}

/* Highlight section being read */
.section-anchor:target {
    background-color: #fff3cd;
    border-left: 4px solid #f0ad4e;
    padding-left: 12px;
}

/* ---------- TOC ---------- */
.toc a {
    color: #555;
    text-decoration: none;
}

.toc a:hover {
    text-decoration: underline;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SECTION DEFINITIONS
# =========================================================
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

# =========================================================
# SESSION STATE
# =========================================================
if "product" not in st.session_state:
    st.session_state.product = "B2B"
if "subproduct" not in st.session_state:
    st.session_state.subproduct = "VA"

# product accordion state
for product in NAV.keys():
    key = f"open_{product}"
    if key not in st.session_state:
        st.session_state[key] = False

# =========================================================
# LAYOUT
# =========================================================
left, center, right = st.columns([2, 4, 2])

# =========================================================
# LEFT SIDEBAR – PRODUCT ACCORDION
# =========================================================
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

        if st.session_state[open_key]:
            for sp in subs.keys():
                is_active = (
                    st.session_state.product == product
                    and st.session_state.subproduct == sp
                )

                if st.button(
                    sp,
                    key=f"sub_{product}_{sp}",
                    use_container_width=True
                ):
                    st.session_state.product = product
                    st.session_state.subproduct = sp
                    st.rerun()

# =========================================================
# RIGHT SIDEBAR – TABLE OF CONTENTS
# =========================================================
with right:
    st.markdown("### Sections")
    st.markdown("<div class='toc'>", unsafe_allow_html=True)

    for sec in NAV[st.session_state.product][st.session_state.subproduct]:
        anchor = sec.lower().replace(" ", "-")
        st.markdown(f"- [{sec}](#{anchor})")

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# CENTER – FULL CONTENT WITH ANCHORS
# =========================================================
with center:
    st.markdown(
        f"##### {st.session_state.product} / {st.session_state.subproduct}"
    )

    sections = NAV[st.session_state.product][st.session_state.subproduct]

    for sec in sections:
        anchor = sec.lower().replace(" ", "-")

        st.markdown(
            f"<div id='{anchor}' class='section-anchor'></div>",
            unsafe_allow_html=True
        )

        st.markdown(f"## {sec}")
        st.divider()

        # ---------- FAKE CONTENT ----------
        st.markdown(f"""
**Description**  
This is mock content for **{sec}** under **{st.session_state.subproduct}**.

**What this section covers**
- Feature explanation
- Integration approach
- Constraints & notes
- Demo-only fake information

**Notes**
All content shown here is for demonstration purposes only.
""")

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

        if sec == "Error Codes":
            st.table(pd.DataFrame({
                "Code": ["400", "401", "403", "500"],
                "Message": [
                    "Bad Request",
                    "Unauthorized",
                    "Forbidden",
                    "Internal Server Error"
                ],
                "Description": [
                    "Invalid input parameters",
                    "Missing or invalid API key",
                    "Access denied",
                    "Unexpected system error"
                ]
            }))
