import streamlit as st
from components.product_sidebar import render_product_sidebar
from components.content_renderer import render_content

st.set_page_config(layout="wide")

if "route" not in st.session_state:
    st.session_state.route = "home"

render_product_sidebar()
render_content(st.session_state.route)
