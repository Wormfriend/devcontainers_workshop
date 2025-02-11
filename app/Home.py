import streamlit as st


PAGE_ICON = "static/devcontainer_logo_transparent.png"

st.session_state["page_icon"] = PAGE_ICON
st.session_state["page_title"] = "Group Meeting"

st.set_page_config(
    page_title=f"{st.session_state.page_title} - Home",
    page_icon=st.session_state.page_icon,
    layout="centered"
)

st.header("Introduction DevContainer")
st.subheader("Escaping Dependency Hell")
st.image("https://imgs.xkcd.com/comics/python_environment.png", use_container_width=True)

column_one, _, column_two = st.columns([2, 5, 2])

with column_two:
    st.page_link("pages/1_Prerequisites.py", label="Next: Prerequisites", use_container_width=True)