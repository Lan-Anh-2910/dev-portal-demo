import streamlit as st

def render_product_sidebar():
    with st.sidebar:
        st.markdown("## Products")

        if st.expander("B2B", expanded=True):
            st.page_link("pages/b2b_va.py", "Virtual Account")
            st.markdown("BNPL")
            st.markdown("Installment")
            st.markdown("Card Payment")

        if st.expander("Bill"):
            st.markdown("Bill Payment")
            st.markdown("Insurance")

        if st.expander("Leadgen"):
            st.markdown("Leadgen")

        if st.expander("Cross-border"):
            st.markdown("Collection")
            st.markdown("Disbursement")
