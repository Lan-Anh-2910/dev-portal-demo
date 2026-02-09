import streamlit as st

def render_section_sidebar(sections):
    st.markdown("### Sections")

    for sec in sections:
        anchor = sec.lower().replace(" ", "-")
        st.markdown(f"- [{sec}](#{anchor})")
