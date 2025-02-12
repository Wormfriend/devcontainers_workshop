import streamlit as st


st.set_page_config(
    page_title=f"{st.session_state.page_title} - Introduction",
    page_icon=st.session_state.page_icon
)


# page content
st.header("Introduction")
st.subheader("Virtualization")

with st.expander("Terminology"):
    st.markdown("""
    - **Operating Systen (OS)**: Operating Systems
        - GNU/Linux
        - Windows
    - **Kernel**: Core of an OS mediating between applications/users and hardware.
    - **Host**: Computer used to virtualize
    - **Guest**: Virtual machine
    """)

with st.expander("Overview"):
    st.markdown("""
    - **Virtualization** is a process, which allows a computer to share its hardware ressources with seperated environments
    - **Virtual Machines** are software defined computers, which can have seperate operating systems and computing ressource (CPU Cores, Memory, ...) 
    """)
    st.image("app/static/hypervisor_types.drawio.svg", caption="Type 1 Hypervisor", use_container_width=True)
    st.markdown("""
    - The **hypervisor manages** virtual machines and most importantly their clear seperation on a hardware level
        - Type 1 Hypervisor: Directly installed on hardware instead of the OS
        - Type 2 Hypervisor: Installed on OS
    """)

st.subheader("Containerization")

with st.expander("Terminology"):
    st.text("CONTENT")

with st.expander("OS Level Virtualization"):
    st.text("CONTENT")

st.subheader("Dev Containers")

with st.expander("Architecture"):
    st.text("CONTENT")
    pass

with st.expander("Advantages"):
    st.markdown("""
    - Clean capsulation of concerns and environments
    - Easy to setup
    - Documentation of installed dependencies and there respective versions
    """)

column_one, _, column_two = st.columns([3, 5, 2])

with column_one:
    st.page_link("pages/1_Prerequisites.py", label="Previous: Prerequisites", use_container_width=True)

with column_two:
    st.page_link("pages/3_Workshop.py", label="Next: Workshop", use_container_width=True)