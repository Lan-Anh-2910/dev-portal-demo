import streamlit as st

def render_product_sidebar():
    with st.sidebar:
        st.markdown("## Products")

        # ================= B2B =================
        with st.expander("B2B", expanded=True):
            if st.button("Virtual Account"):
                st.session_state.route = "b2b_va"

            st.markdown("BNPL")
            st.markdown("Installment")
            st.markdown("Card Payment")

        # ================= Bill =================
        with st.expander("Bill"):
            st.markdown("Bill Payment")
            st.markdown("Insurance")

        # ================= Leadgen =================
        with st.expander("Leadgen"):
            st.markdown("Leadgen")

        # ================= Cross-border =================
        with st.expander("Cross-border"):
            st.markdown("Collection")
            st.markdown("Disbursement")
            st.markdown("Check transaction status")
            st.markdown("Check balance")
            st.markdown("Payment")
            st.markdown("Refund")
            st.markdown("Settlement")
            st.markdown("Onboarding sellers")
