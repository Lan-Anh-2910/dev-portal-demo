import streamlit as st

def render_breadcrumbs(items):
    """
    items = [
      {"label": "B2B", "route": "home"},
      {"label": "VA", "route": "b2b_va"},
      {"label": "Direct Merchant", "route": "b2b_va"},
      {"label": "Basic", "route": "b2b_va_direct_basic"}
    ]
    """
    cols = st.columns(len(items) * 2 - 1)

    col_idx = 0
    for i, item in enumerate(items):
        with cols[col_idx]:
            if i < len(items) - 1:
                if st.button(item["label"], key=f"bc_{item['label']}"):
                    st.session_state.route = item["route"]
            else:
                st.markdown(f"**{item['label']}**")

        col_idx += 1

        if i < len(items) - 1:
            with cols[col_idx]:
                st.markdown(">")
            col_idx += 1
