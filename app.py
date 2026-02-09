import streamlit as st

st.set_page_config(
page_title="Dev Portal Demo - B2B VA",
layout="wide"
)

st.markdown("""

<style> :target { scroll-margin-top: 90px; } .section-anchor:target { background-color: #fff3cd; border-left: 4px solid #f0ad4e; padding-left: 12px; } .usecase-card { padding: 16px; border: 1px solid #e6e6e6; border-radius: 10px; background: #fafafa; height: 100%; } .usecase-card h3 { margin-top: 0; } .integration-box { padding: 14px; border-radius: 8px; background: #f8f9fa; margin-bottom: 16px; } </style>

""", unsafe_allow_html=True)

st.title("B2B / Virtual Account (VA)")
st.caption("Demo API Documentation – Mock content for internal presentation")

st.divider()

st.markdown("## Overview")

st.markdown("""
Virtual Account (VA) allows merchants to receive payments through
unique bank account numbers generated for each customer or transaction.

This documentation helps you:

Identify your business model

Choose the correct integration method

Implement VA payment efficiently
""")

st.divider()

st.markdown("## Use case")
st.markdown("<div class='section-anchor' id='use-case'></div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
st.markdown("<div class='usecase-card'>", unsafe_allow_html=True)
st.markdown("### Direct Merchant")

st.markdown("""


Who is this for?

Merchants selling their own products or services

One merchant account

No sub-merchants involved

Typical scenarios

E-commerce website

Subscription services

Service providers

Integration flow
Customer
↓
Merchant Website / App
↓
Payment Gateway
↓
Bank

Recommended integration methods

Basic Integration → #basic-integration

Pro Integration → #pro-integration
""")
st.markdown("</div>", unsafe_allow_html=True)

with col2:
st.markdown("<div class='usecase-card'>", unsafe_allow_html=True)
st.markdown("### Master Merchant")

st.markdown("""


Who is this for?

Platforms or marketplaces

Managing multiple sub-merchants

Collecting payments on behalf of others

Typical scenarios

Marketplace platforms

Super Apps

SaaS platforms with sellers

Integration flow
Customer
↓
Platform (Master Merchant)
↓
Payment Gateway
↓
Bank

Recommended integration methods

Pro Integration → #pro-integration

Host to Host Integration → #host-to-host
""")
st.markdown("</div>", unsafe_allow_html=True)

st.divider()

st.markdown("## Integrate Methods")

st.markdown("<div id='basic-integration' class='section-anchor'></div>", unsafe_allow_html=True)
st.markdown("### Basic Integration")

st.markdown("""
Best for

Direct Merchant

MVP or quick launch

Characteristics

Redirect or SDK-based

Minimal API implementation

Fast time to market

Limitations

Limited UI customization

Dependent on payment gateway UI
""")

st.markdown("<div id='pro-integration' class='section-anchor'></div>", unsafe_allow_html=True)
st.markdown("### Pro Integration")

st.markdown("""
Best for

Direct Merchant (advanced)

Master Merchant

Characteristics

Full API integration

Custom checkout experience

Better control over payment flow

Requirements

Backend integration

Webhook handling
""")

st.markdown("<div id='host-to-host' class='section-anchor'></div>", unsafe_allow_html=True)
st.markdown("### Host to Host Integration")

st.markdown("""
Best for

Master Merchant

Enterprise platforms

Characteristics

Server-to-server communication

No redirect

Highest security level

Requirements

IP whitelisting

Security review

Technical onboarding process
""")

st.divider()

st.markdown("## Next steps")

st.markdown("""

Identify your Use case

Select the appropriate Integration Method

Proceed to Sandbox for testing

Review API Reference for implementation details
""")

st.success("All content shown is mock data for demo purposes only.")
