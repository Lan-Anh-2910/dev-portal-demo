import streamlit as st

def render_product_sidebar():
    with st.sidebar:
        st.markdown("## Products")

        with st.expander("B2B", expanded=True):
            st.page_link("pages/b2b_va.py", label="Virtual Account")
            st.markdown("BNPL")
            st.markdown("Installment")
            st.markdown("Card Payment")

        with st.expander("Bill"):
            st.markdown("Bill Payment")
            st.markdown("Insurance")

        with st.expander("Leadgen"):
            st.markdown("Leadgen")

        with st.expander("Cross-border"):
            st.markdown("Collection")
            st.markdown("Disbursement")
