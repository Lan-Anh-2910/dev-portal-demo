import streamlit as st

st.set_page_config(layout="wide")

if "page" not in st.session_state:
    st.session_state.page = "b2b_va"

# ========== LEFT NAV ==========
with st.sidebar:
    st.title("Dev Portal")

    with st.expander("B2B", expanded=True):
        if st.button("VA"):
            st.session_state.page = "b2b_va"
        if st.button("BNPL"):
            st.session_state.page = "b2b_bnpl"
        if st.button("Installment"):
            st.session_state.page = "b2b_installment"
        if st.button("Card Payment"):
            st.session_state.page = "b2b_card"

    with st.expander("Bill"):
        if st.button("Bill Payment"):
            st.session_state.page = "bill_payment"
        if st.button("Insurance"):
            st.session_state.page = "bill_insurance"

    if st.button("Leadgen"):
        st.session_state.page = "leadgen"

    with st.expander("Cross-border"):
        if st.button("Collection"):
            st.session_state.page = "cb_collection"
        if st.button("Disbursement"):
            st.session_state.page = "cb_disbursement"
        if st.button("Payment"):
            st.session_state.page = "cb_payment"

# ========== PAGE ROUTER ==========
page = st.session_state.page

if page == "b2b_va":
    import pages.b2b_va as page_file
elif page == "b2b_bnpl":
    import pages.b2b_bnpl as page_file
elif page == "b2b_installment":
    import pages.b2b_installment as page_file
elif page == "b2b_card":
    import pages.b2b_card as page_file
elif page == "bill_payment":
    import pages.bill_payment as page_file
elif page == "bill_insurance":
    import pages.bill_insurance as page_file
elif page == "leadgen":
    import pages.leadgen as page_file
elif page == "cb_collection":
    import pages.cb_collection as page_file
elif page == "cb_disbursement":
    import pages.cb_disbursement as page_file
elif page == "cb_payment":
    import pages.cb_payment as page_file

page_file.render()
