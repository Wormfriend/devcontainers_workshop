import streamlit as st


PAGE_ICON = "app/static/devcontainer_logo_transparent.png"
PAGE_TITLE = "Group Meeting"

st.set_page_config(
    page_title=f"{PAGE_TITLE} - Prerequisites",
    page_icon=PAGE_ICON,
    layout="centered"
)
st.logo("app/static/sidebar_logo.png", size="large")

st.header("Prerequisites")

with st.expander("Setup Docker Desktop"):
    st.markdown(
        "Installation instructions for Docker Desktop on Mac can be found " 
        "[here](https://docs.docker.com/desktop/setup/install/mac-install/). "
        "Since most people (if not all) in our group have more recent Macs base on ARM "
        "(Apple Silicon) you can use the **Docker Desktop for Mac with Apple silicon** "
        "download button on top of the page. After downloading follow the "
        "[installation instructions](https://docs.docker.com/desktop/setup/install/mac-install/#install-and-run-docker-desktop-on-mac)."
    )
    
with st.expander("Setup VS Code"):
    st.markdown(
        "Installation instructions for VScode can be found [here](https://code.visualstudio.com/docs/setup/mac) "
        "here. After download and installation I can highly recommend the installation "
        "of the official python extension (linter, debugger) from the marketplace. "
    )
    st.image("app/static/vscode_extension.png", caption="VSCode Python Extension")

with st.expander("Install DevContainer Extension"):
    st.markdown(
        "Alike the Python extension, the DevContainers extension can also be installed "
        "from the VSCode marketplace accessible through the sidebar within VSCode."
    )
    st.image("app/static/vscode_devcontainers_extension.png", caption="VSCode DevContainers Extension")


column_one, _, column_two = st.columns([2, 5, 2])

with column_one:
    st.page_link("Home.py", label="Previous: Home", use_container_width=True)

with column_two:
    st.page_link("pages/2_Introduction.py", label="Next: Introduction", use_container_width=True)
