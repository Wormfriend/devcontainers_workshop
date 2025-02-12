from datetime import datetime, timezone
import streamlit as st


st.set_page_config(
    page_title=f"{st.session_state.page_title} - Workshop",
    page_icon=st.session_state.page_icon
)

st.header("Workshop")


with st.expander("Create A Dockerfile"):
    st.markdown("""
    ```dockerfile
    # DevcontainersWorkshop/Dockerfile
    FROM python:3.12            # Specify base image
    ```
    """)

with st.expander("Create A devcontainer.json"):
    st.write("YOUR TEXT HERE")
    st.markdown("""
    Your final file structure should look like the following:
    ```bash
    DevcontainersWorkshop
    ├── Dockerfile
    ├── .devcontainers
        ├── devontainer.json
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
