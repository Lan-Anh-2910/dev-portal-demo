import streamlit as st

def render_product_sidebar():
    with st.sidebar:
        st.markdown("## Products")

        with st.expander("B2B", expanded=True):
            st.page_link(
                page="b2b_va",
                label="Virtual Account"
            )
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
