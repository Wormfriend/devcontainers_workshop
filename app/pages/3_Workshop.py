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
        "DevContainers you have installed as part of the [Prerequisites](/Prerequisites)."
    )
    st.markdown("**Step 1 - Open Dev Container Extension**")
    st.text("Click on the blue icon in the bottom left corner of VSCode.")
    st.image("app/static/vscode_open_devcontainer_extension.png", caption="Opening Dev Container Extension")
    st.markdown("**Step 2 - Create devcontainer.json from Dockerfile**")
    st.markdown(
        "In the menu opening in the top middle click *Add Dev Container Configuration Files...*. "
        "Then select *From 'Dockerfile'*. Afterwards do not select any additional features - just click *ok*. "
        "This should then create a ```.devcontainer/``` directory containing a single ```devcontainer.json``` file."
    )
    st.image("app/static/vscode_add_config.png", caption="Select Add Dev Container Configuration Files...")
    st.image("app/static/vscode_from_dockerfile.png", caption="Select From 'Dockerfile'")
    st.image("app/static/vscode_select_features.png", caption="Click OK")
    st.markdown("Your *devcontainer.json* is supposed to look like this:")
    st.code("""
    // .devcontainer/devcontainer.json
    // For format details, see https://aka.ms/devcontainer.json. For config options, see the
    // README at: https://github.com/devcontainers/templates/tree/main/src/docker-existing-dockerfile
    {
        "name": "Existing Dockerfile",
        "build": {
            // Sets the run context to one level up instead of the .devcontainer folder.
            "context": "..",
            // Update the 'dockerFile' property if you aren't using the standard 'Dockerfile' filename.
            "dockerfile": "../Dockerfile"
        }

        // Features to add to the dev container. More info: https://containers.dev/features.
        // "features": {},

        // Use 'forwardPorts' to make a list of ports inside the container available locally.
        // "forwardPorts": [],

        // Uncomment the next line to run commands after the container is created.
        // "postCreateCommand": "cat /etc/os-release",

        // Configure tool-specific properties.
        // "customizations": {},

        // Uncomment to connect as an existing user other than the container default. More info: https://aka.ms/dev-containers-non-root.
        // "remoteUser": "devcontainer"
    }
    """, 
    language="json"
    )
    st.markdown("""
    Your file tree should now look like the following.
    ```bash
    DevcontainersWorkshop
    ├── Dockerfile
    ├── .devcontainer
        ├── devontainer.json
    ```
    """)

with st.expander("Add Python Extension To Dev Container"):
    st.markdown("Search for the official *Python* Extension in the Extension Menu on the left of your VSCode Window. ")
    st.text("Right click on the extension and select *Add to devcontainer.json*.")
    st.image("app/static/vscode_extension_python.png", caption="Add Python Extension to devcontainer.json")
    st.markdown("Your *devcontainer.json* should now be edited and contain the section below:")
    st.code("""
    {
        // ... 
        "customizations": {
            "vscode": {
                "extensions": [
                    "ms-python.python"
                ]
            }
        }
        // ...
    }
    """, language="json")

with st.expander("Create requirements.txt"):
    st.markdown("Now create a *requirements.txt file. This file will contain your python dependencies.")
    st.code("touch requirements.txt", language="bash")
    st.text("Copy the text below into the created file.")
    st.code("""
    # DevContainerWorkshop/requirements.txt
    streamlit==1.42.0
    """, language="bash")
    st.markdown("""
    Afterwards your project structure should look like the following.
    ```bash
    DevcontainersWorkshop
    ├── Dockerfile
    ├── .devcontainer
        ├── devontainer.json
    ├── requirements.txt
    ```
    """)

with st.expander("Edit Your Dockerfile"):
    st.markdown("Now it is time to finally make your *Dockerfile* good to go. Copy the below into your Dockerfile.")
    st.markdown("""
    ```dockerfile
    # DevcontainersWorkshop/Dockerfile
    # Specify base image
    FROM python:3.12                

    # Copies the hosts ./requirements.txt into your guests /tmp 
    COPY requirements.txt /tmp
    # Install the dependencies using pip
    RUN python -m pip install -r /tmp/requirements.txt
    ```
    """)

with st.expander("Start your devcontainer"):
    st.markdown(
        "In the bottom left click on the blue icon again. In the menu select *Reopen in Container*. "
        "This step might take some time since docker is now downloading the python base image from "
        "Dockerhub and afterwards installs streamlit from the Python Package Index ([PyPI](https://pypi.org))."
    )
    st.image("app/static/vscode_reopen_in_container.png", caption="Start Dev Container")

with st.expander("Create 'Hello Streamlit' application"):
    st.markdown(
        "Once you are within your Dev Container create a new directory called *app* and within this create file "
        "named *index.py*"
    )
    st.code("""
    mkdir app
    touch app/index.py
    """,
    language="bash")
    st.markdown("Add the following lines of code to your *index.py* file.")
    st.code("""
    # app/index.py
    import streamlit as st


    st.header("Hello From Streamlit")
    st.balloons()
    """, language="python")
    st.markdown(
        ">In case you get an import error select the correct python version in the bottom right of VSCode." 
        "For this workshop it is Python 3.12."
    )

    st.markdown("""
    Your final file tree is supposed to look like this:
    ```bash
    DevcontainersWorkshop
    ├── Dockerfile
    ├── .devcontainer
        ├── devontainer.json
    ├── requirements.txt
    ├── app
        ├── index.py
    ```
    """)
    st.text("You can now execute your application.")
    st.code("""
    cd app/
    streamlit run app.py
    """, language="bash")
    st.text(
        "Since DevContainers takes care of all port-forwarding for you, you can now vist your application under the URL shown in your terminal."
    )

# footer
column_one, _, column_two = st.columns([3, 4, 2])

with column_one:
    st.page_link("pages/2_Introduction.py", label="Previous: Introduction", use_container_width=True)

with column_two:
    st.page_link("pages/4_Ressources.py", label="Next: Ressources", use_container_width=True)
