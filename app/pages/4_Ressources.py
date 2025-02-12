import streamlit as st


st.set_page_config(
    page_title=f"{st.session_state.page_title} - Ressources",
    page_icon=st.session_state.page_icon,
)

st.header("Ressources")
st.link_button(
    "Metadata Reference: devcontainer.json ",
    "https://containers.dev/implementors/json_reference/",
)
st.link_button(
    "Installation Instructions Docker Desktop",
    "https://docs.docker.com/desktop/setup/install/mac-install/",
)
st.link_button(
    "Installation Instructions VSCode", "https://code.visualstudio.com/docs/setup/mac"
)
st.link_button("Dockerhub", "https://hub.docker.com/")
st.link_button(
    "VSCode Extension Marketplace", "https://marketplace.visualstudio.com/vscode"
)
st.link_button(
    "Wikipedia: Virtualization", "https://en.wikipedia.org/wiki/Virtualization"
)
st.link_button(
    "Wikipedia: OS-level Virtualization",
    "https://en.wikipedia.org/wiki/OS-level_virtualization",
)
st.link_button(
    "Wikipedia: Kernel", "https://en.wikipedia.org/wiki/Kernel_(operating_system)"
)
st.link_button(
    "Techtarget: What is a kernel?",
    "https://www.techtarget.com/searchdatacenter/definition/kernel",
)
st.link_button(
    "AWS: What is virtualization", "https://aws.amazon.com/what-is/virtualization/"
)
st.link_button(
    "Digihunch: Overview Virtualization",
    "https://www.digihunch.com/2020/07/overview-of-virtualization/",
)
st.link_button(
    "Stackoverflow: Difference Emulation and Virtualization:",
    "https://stackoverflow.com/questions/6234711/what-are-the-specific-differences-between-an-emulator-and-a-virtual-machine",
)
st.link_button(
    "VSCode Devcontainers: Official Docs",
    "https://code.visualstudio.com/docs/devcontainers/containers"
)

st.page_link("pages/3_Workshop.py", label="Previous: Workshop")
