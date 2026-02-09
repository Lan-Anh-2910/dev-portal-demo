import streamlit as st

st.set_page_config(page_title="B2B - Virtual Account", layout="wide")

# ===== Breadcrumb =====
st.markdown("**B2B > Virtual Account**")

st.title("Virtual Account (VA)")

# ===== Overview =====
st.header("Overview")
st.write("""
Virtual Account (VA) allows merchants to collect payments using unique virtual account numbers.
This page helps you choose the correct integration based on your business model.
""")

# ===== Use case =====
st.header("Use case")

st.subheader("Direct Merchant")
st.write("""
You are a Direct Merchant if you collect payments directly from end users
and do not manage sub-merchants.
""")

st.subheader("Master Merchant")
st.write("""
You are a Master Merchant if you operate a platform or marketplace
and manage multiple sub-merchants.
""")

# ===== Integration Methods =====
st.header("Integration Methods")

st.subheader("Direct Merchant")

st.page_link(
    "pages/b2b_va_direct_basic.py",
    label="➡️ Basic Integration",
)

st.page_link(
    "pages/b2b_va_direct_h2h.py",
    label="➡️ Host-to-Host Integration",
)

st.subheader("Master Merchant")

st.page_link(
    "pages/b2b_va_master_basic.py",
    label="➡️ Basic Integration",
)

st.page_link(
    "pages/b2b_va_master_h2h.py",
    label="➡️ Host-to-Host Integration",
)
