import streamlit as st

def render_section_sidebar(sections):
    st.markdown("### Sections")
    for sec in sections:
        st.markdown(f"- {sec}")
