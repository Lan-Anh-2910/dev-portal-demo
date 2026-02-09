import streamlit as st

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Dev Portal Demo - B2B VA",
    layout="wide"
)

# =========================================================
# GLOBAL CSS
# =========================================================
st.markdown("""
<style>
:target {
    scroll-margin-top: 90px;
}

.section-anchor:target {
    background-color: #fff3cd;
    border-left: 4px solid #f0ad4e;
    padding-left: 12px;
}

.usecase-card {
    padding: 16px;
    border: 1px solid #e6e6e6;
    border-radius: 10px;
    background: #fafafa;
    height: 100%;
}

.usecase-card h3 {
    margin-top: 0;
}

.integration-box {
    padding: 14px;
    border-radius: 8px;
    background: #f8f9fa;
    margin-bottom: 16px;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
st.title("B2B / Virtual Account (VA)")
st.caption("Demo API Documentation – Mock content for internal presentation")

st.divider()

# =========================================================
# OVERVIEW
# =========================================================
st.markdown("## Overview")

st.markdown("""
Virtual Account (VA) allows merchants to receive payments through
unique bank account numbers generated for each customer or transaction.

This documentation helps you:
- Identify your business model
- Choose the correct integration method
- Implement VA payment efficiently
""")

st.divider()

# =========================================================
# USE CASE
# =========================================================
st.markdown("## Use case")
st.markdown("<div class='section-anchor' id='use-case'></div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# -----------------------
# DIRECT MERCHANT
# -----------------------
with col1:
    st.markdown("<div class='usecase-card'>", unsafe_allow_html=True)
    st.markdown("### Direct Merchant")

    st.markdown("""
**Who is this for?**
- Merchants selling their **own products or services**
- One merchant account
- No sub-merchants involved

**Typical scenarios**
- E-commerce website
- Subscription services
- Service providers

**Integration flow**
