import streamlit as st
from components.product_sidebar import render_product_sidebar

st.set_page_config(layout="wide")

render_product_sidebar()

st.title("Developer Portal")
st.write("Select a product to start from the content area.")
