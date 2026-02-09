import streamlit as st

def render_section_sidebar(sections):
    with st.container():
        st.markdown("### Sections")
        for s in sections:
            st.markdown(f"- [{s}](#{s.lower().replace(' ', '-')})")
