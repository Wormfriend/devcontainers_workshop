import streamlit as st


PAGE_ICON = "app/static/devcontainer_logo_transparent.png"
PAGE_TITLE = "Group Meeting"

st.set_page_config(
    page_title=f"{PAGE_TITLE} - Home",
    page_icon=PAGE_ICON,
    layout="centered"
)
st.logo("app/static/sidebar_logo.png", size="large")

st.header("Introduction DevContainer")
st.subheader("Escaping Dependency Hell")
st.image("https://imgs.xkcd.com/comics/python_environment.png", use_container_width=True)
st.subheader("Preamble")
st.markdown(
    "This website is part of a short workshop held at the " 
    "[University Clinic Freiburg](https://www.uniklinik-freiburg.de/de.html) on "
    "February 14<sup>th</sup> 2025. Due to the one hour format of this workshop it does "
    "not claim to be complete by any means. For a deeper dive into DevContainers please "
    "visit the list of [ressources](/Ressources) at the end of this page.",
    unsafe_allow_html=True
)

column_one, _, column_two = st.columns([2, 5, 2])

with column_two:
    st.page_link("pages/1_Prerequisites.py", label="Next: Prerequisites", use_container_width=True)