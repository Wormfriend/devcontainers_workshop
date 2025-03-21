import streamlit as st


PAGE_ICON = "app/static/devcontainer_logo_transparent.png"
PAGE_TITLE = "Group Meeting"

st.set_page_config(
    page_title=f"{PAGE_TITLE} - Ressources",
    page_icon=PAGE_ICON,
    layout="centered"
)
st.logo("app/static/sidebar_logo.png", size="large")

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
    "Stackoverflow: Difference Emulation and Virtualization",
    "https://stackoverflow.com/questions/6234711/what-are-the-specific-differences-between-an-emulator-and-a-virtual-machine",
)
st.link_button(
    "VSCode Devcontainers: Official Docs",
    "https://code.visualstudio.com/docs/devcontainers/containers"
)
st.link_button(
    "The Customize Windows: How OS-Level Virtualization Works",
    "https://thecustomizewindows.com/2023/03/how-os-level-virtualization-works/"
)
st.link_button(
    "Wikipedia: chroot",
    "https://en.wikipedia.org/wiki/Chroot"
)
st.link_button(
    "Linux man page: chroot",
    "https://linux.die.net/man/1/chroot"
)
st.link_button(
    "elprocus: What is an Operating System and Its Components",
    "https://www.elprocus.com/what-is-an-operating-system-and-its-components/"
)
st.link_button(
    "Flylib: Linux Kernel Structure",
    "https://flylib.com/books/en/3.475.1.15/1/"
)
st.link_button(
    "Docker Docs: Docker Overview",
    "https://docs.docker.com/get-started/docker-overview/"
)

st.page_link("pages/3_Workshop.py", label="Previous: Workshop")
