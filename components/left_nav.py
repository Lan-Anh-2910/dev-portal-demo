import streamlit as st

def render_left_nav():
    st.markdown("### Products")

    with st.expander("B2B", expanded=True):
        if st.button("VA", use_container_width=True):
            st.session_state.selected_page = "B2B_VA"

        st.markdown("BNPL")
        st.markdown("Installment")
        st.markdown("Card Payment")

    with st.expander("Bill"):
        st.markdown("Bill Payment")
        st.markdown("Insurance")

    st.divider()
