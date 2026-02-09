import streamlit as st

def nav_item(label, page_key):
    if st.button(label, key=page_key, use_container_width=True):
        st.session_state.selected_page = page_key

def render_left_nav():
    st.markdown("### Products")

    with st.expander("B2B", expanded=True):
        nav_item("VA", "B2B_VA")
        nav_item("BNPL", "B2B_BNPL")
        nav_item("Installment", "B2B_INSTALLMENT")
        nav_item("Card Payment", "B2B_CARD")

    with st.expander("Bill"):
        nav_item("Bill Payment", "BILL_PAYMENT")
        nav_item("Insurance", "BILL_INSURANCE")

    st.markdown("### Leadgen")

    with st.expander("Cross-border"):
        nav_item("Collection", "CB_COLLECTION")
        nav_item("Disbursement", "CB_DISBURSEMENT")
        nav_item("Check transaction status", "CB_CHECK_TX")
        nav_item("Check balance", "CB_CHECK_BALANCE")
        nav_item("Payment", "CB_PAYMENT")
        nav_item("Refund", "CB_REFUND")
        nav_item("Settlement", "CB_SETTLEMENT")
        nav_item("Onboarding sellers", "CB_ONBOARDING")
