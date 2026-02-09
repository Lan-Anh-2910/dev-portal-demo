import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dev Portal Demo", layout="wide")

# ---------- DATA STRUCTURE ----------
NAV = {
    "B2B": {
        "VA": ["Overview", "Use case", "Sandbox", "API Reference", "Webhook", "Error Codes"],
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
left, center, right = st.columns([1.6, 3.8, 1.6])

# ---------- LEFT: PRODUCT + SUBPRODUCT ----------
with left:
    st.markdown("### Products")

    for product, subs in NAV.items():
        st.markdown(f"**{product}**")

        choice = st.radio(
            "",
            list(subs.keys()),
            key=f"sub_{product}",
            label_visibility="collapsed"
        )

        if choice:
            st.session_state.product_
