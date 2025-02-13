from datetime import datetime, timezone
import streamlit as st


PAGE_ICON = "app/static/devcontainer_logo_transparent.png"
PAGE_TITLE = "Group Meeting"

st.set_page_config(
    page_title=f"{PAGE_TITLE} - Workshop",
    page_icon=PAGE_ICON,
    layout="centered"
)
st.logo("app/static/sidebar_logo.png", size="large")

st.header("Workshop")

with st.expander("Create A Project Directory"):
    st.write("Start by creating a directory for your project. Start VSCode within.")
    st.code(
        """
        mkdir DevContainerWorkshop
        touch DevContainerWorkshop/Dockerfile
        code DevContainerWorkshop
        """, 
        language="bash"
    )
    st.markdown(
        ">If the ```code``` command does not seem to work for you you might need "
        "to follow [this](https://code.visualstudio.com/docs/setup/mac#_launch-vs-code-from-the-command-line) "
        "additional steps. Or navigate to your directory from within the VSCode GUI."
    )
    st.markdown("""
    Afterwards your file tree should look something like the following.
    ```bash
    DevcontainersWorkshop
    ├── Dockerfile
    ```
    """)

with st.expander("Create A devcontainer.json"):
    st.markdown(
        "The easiest way for creating a devcontainer-configuration is using the "
        "DevContainers you have installed as part of the [Prerequisites](/Prerequisites). "
    )
    st.markdown("""
    Your final file structure should look like the following:
    ```bash
    DevcontainersWorkshop
    ├── Dockerfile
    ├── .devcontainers
        ├── devontainer.json
    ```
    """)

with st.expander("Edit Your Dockerfile"):
    st.markdown("""
    ```dockerfile
    # DevcontainersWorkshop/Dockerfile
    FROM python:3.12            # Specify base image
    ```
    """)


with st.expander("Add your favourite extensions"):
    st.write("YOUR TEXT HERE")

with st.expander("Create requirements.txt"):
    st.write("YOUR TEXT HERE")

with st.expander("Start your devcontainer"):
    st.write("YOUR TEXT HERE")

with st.expander("Clone Git-Repository"):
    st.write("YOUR TEXT HERE")

with st.expander("Deploy application as Docker-container"):
    st.write("YOUR TEXT HERE")


# footer
column_one, _, column_two = st.columns([3, 4, 2])

with column_one:
    st.page_link("pages/2_Introduction.py", label="Previous: Introduction", use_container_width=True)

with column_two:
    st.page_link("pages/4_Ressources.py", label="Next: Ressources", use_container_width=True)
