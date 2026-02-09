import streamlit as st

st.set_page_config(page_title="B2B - VA", layout="wide")

# ===== LAYOUT: LEFT | CENTER | RIGHT =====
left, center, right = st.columns([1.3, 4.5, 1.2])

# ===== LEFT: PRODUCT / SUBPRODUCT =====
with left:
    st.markdown("### Products")
    st.markdown("**B2B**")
    st.markdown("- Virtual Account")
    st.markdown("- BNPL")
    st.markdown("- Installment")
    st.markdown("- Card Payment")

# ===== RIGHT: SECTION NAV =====
with right:
    st.markdown("### Sections")
    st.markdown("- [Overview](#overview)")
    st.markdown("- [Use case](#use-case)")
    st.markdown("- [Integration Methods](#integration-methods)")

# ===== CENTER: CONTENT =====
with center:
    st.markdown("**B2B > Virtual Account**")
    st.title("Virtual Account (VA)")

    st.markdown('<a name="overview"></a>', unsafe_allow_html=True)
    st.header("Overview")
    st.write("Virtual Account enables merchants to collect payments via unique account numbers.")

    st.markdown('<a name="use-case"></a>', unsafe_allow_html=True)
    st.header("Use case")

    st.subheader("Direct Merchant")
    st.write("Collect payments directly from end users.")

    st.subheader("Master Merchant")
    st.write("Operate a platform managing sub-merchants.")

    st.markdown('<a name="integration-methods"></a>', unsafe_allow_html=True)
    st.header("Integration Methods")

    st.subheader("Direct Merchant")
    st.page_link("pages/b2b_va_direct_basic.py", "➡️ Direct MRC / Basic")
    st.page_link("pages/b2b_va_direct_h2h.py", "➡️ Direct MRC / Host-to-Host")

    st.subheader("Master Merchant")
    st.page_link("pages/b2b_va_master_basic.py", "➡️ Master MRC / Basic")
    st.page_link("pages/b2b_va_master_h2h.py", "➡️ Master MRC / Host-to-Host")
