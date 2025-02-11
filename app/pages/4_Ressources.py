import streamlit as st


st.set_page_config(
    page_title=f"{st.session_state.page_title} - Ressources",
    page_icon=st.session_state.page_icon
)

st.header("Ressources")
st.link_button("Metadata Reference: devcontainer.json ", "https://containers.dev/implementors/json_reference/")
st.link_button("Installation Instructions Docker Desktop", "https://docs.docker.com/desktop/setup/install/mac-install/")
st.link_button("Installation Instructions VSCode", "https://code.visualstudio.com/docs/setup/mac")
st.link_button("Dockerhub", "https://hub.docker.com/")
st.link_button("VSCode Extension Marketplace", "https://marketplace.visualstudio.com/vscode")
st.link_button("Wikiepdia: Virtualization", "https://en.wikipedia.org/wiki/Virtualization")
st.link_button("Wikiepdia: OS-level Virtualization", "https://en.wikipedia.org/wiki/OS-level_virtualization")

st.page_link("pages/3_Workshop.py", label="Previous: Workshop")
