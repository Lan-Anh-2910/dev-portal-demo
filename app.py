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
Customer
↓
Merchant Website / App
↓
Payment Gateway
↓
Bank

markdown
Sao chép mã

**Recommended integration methods**
- 🔗 [Basic Integration](#basic-integration)
- 🔗 [Pro Integration](#pro-integration)
""")
    st.markdown("</div>", unsafe_allow_html=True)

# -----------------------
# MASTER MERCHANT
# -----------------------
with col2:
    st.markdown("<div class='usecase-card'>", unsafe_allow_html=True)
    st.markdown("### Master Merchant")

    st.markdown("""
**Who is this for?**
- Platforms or marketplaces
- Managing **multiple sub-merchants**
- Collecting payments on behalf of others

**Typical scenarios**
- Marketplace platforms
- Super Apps
- SaaS platforms with sellers

**Integration flow**
Customer
↓
Platform (Master Merchant)
↓
Payment Gateway
↓
Bank

pgsql
Sao chép mã

**Recommended integration methods**
- 🔗 [Pro Integration](#pro-integration)
- 🔗 [Host to Host Integration](#host-to-host)
""")
    st.markdown("</div>", unsafe_allow_html=True)

st.divider()

# =========================================================
# INTEGRATE METHODS
# =========================================================
st.markdown("## Integrate Methods")

# -----------------------
# BASIC
# -----------------------
st.markdown("<div id='basic-integration' class='section-anchor'></div>", unsafe_allow_html=True)
st.markdown("### Basic Integration")

st.markdown("""
<div class="integration-box">

**Best for**
- Direct Merchant
- MVP or quick launch

**Characteristics**
- Redirect or SDK-based
- Minimal API implementation
- Fast time to market

**Limitations**
- Limited UI customization
- Dependent on payment gateway UI

</div>
""", unsafe_allow_html=True)

# -----------------------
# PRO
# -----------------------
st.markdown("<div id='pro-integration' class='section-anchor'></div>", unsafe_allow_html=True)
st.markdown("### Pro Integration")

st.markdown("""
<div class="integration-box">

**Best for**
- Direct Merchant (advanced)
- Master Merchant

**Characteristics**
- Full API integration
- Custom checkout experience
- Better control over payment flow

**Requirements**
- Backend integration
- Webhook handling

</div>
""", unsafe_allow_html=True)

# -----------------------
# HOST TO HOST
# -----------------------
st.markdown("<div id='host-to-host' class='section-anchor'></div>", unsafe_allow_html=True)
st.markdown("### Host to Host Integration")

st.markdown("""
<div class="integration-box">

**Best for**
- Master Merchant
- Enterprise platforms

**Characteristics**
- Server-to-server communication
- No redirect
- Highest security level

**Requirements**
- IP whitelisting
- Security review
- Technical onboarding process

</div>
""", unsafe_allow_html=True)

st.divider()

# =========================================================
# NEXT STEPS
# =========================================================
st.markdown("## Next steps")

st.markdown("""
1. Identify your **Use case**
2. Select the appropriate **Integration Method**
3. Proceed to **Sandbox** for testing
4. Review **API Reference** for implementation details
""")

st.success("All content shown is mock data for demo purposes only.")
