import streamlit as st
from components.product_sidebar import render_product_sidebar

st.set_page_config(layout="wide")

# SIDEBAR TRÁI (PRODUCT)
render_product_sidebar()

# CONTENT
st.title("Developer Portal")
st.write("Select a product from the left menu")
