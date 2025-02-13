import streamlit as st


PAGE_ICON = "app/static/devcontainer_logo_transparent.png"
PAGE_TITLE = "Group Meeting"

st.set_page_config(
    page_title=f"{PAGE_TITLE} - Introduction",
    page_icon=PAGE_ICON,
    layout="centered"
)
st.logo("app/static/sidebar_logo.png", size="large")

# page content
st.header("Introduction")
st.subheader("Full Virtualization")

with st.expander("Terminology"):
    st.markdown(
        """
    - **Operating Systen (OS)**: Operating Systems
        - GNU/Linux
        - Windows
    - **Kernel**: Core of an OS mediating between applications/users and hardware.
    - **Host**: Computer used to virtualize
    - **Guest**: Virtual machine
    """
    )

with st.expander("Overview"):
    st.markdown(
        """
    - **Virtualization** is a process, which allows a computer to share its hardware ressources with seperated environments
    - **Virtual Machines** are software defined computers, which can have seperate operating systems and computing ressource (CPU Cores, Memory, ...) 
    """
    )
    st.image(
        "app/static/hypervisor_types.drawio.svg",
        caption="Hypervisor Types",
        use_container_width=True,
    )
    st.markdown(
        """
    - The **hypervisor manages** virtual machines and most importantly their clear seperation on a hardware level
        - Type 1 Hypervisor: Directly installed on hardware instead of the OS
        - Type 2 Hypervisor: Installed on OS
    """
    )

st.subheader("Containerization")

with st.expander("Terminology"):
    st.markdown("""
    - **User Space**: All code outside of the kernel
    - **Container**: An additional userspace instance
    - **Docker**: A product, which combines a set of tools to virtualize containers
    """)

with st.expander("Overview"):
    st.markdown("""
    - Containerization describes application- or OS-level virtualization
    """)
    st.image("app/static/os_level_virtualization.drawio.svg", use_container_width=True, caption="OS-Level Virtualization")
    st.markdown("""
    - Multiple instances of guest operating systems (at least the user space part) share a host kernel - in contrary of fully VMs
    - Historically originated from the [chroot](https://linux.die.net/man/1/chroot) unix system call
    - Became popular with the broader adaption of [Docker](https://www.docker.com/)
    - A program (or a bundle which make up an entire OS) are only granted access to a subset of ressources available to the host OS
    """)
    st.image("app/static/linux_kernel.drawio.svg", use_container_width=True, caption="Linux Kernel")
    st.markdown("""
    - Containerization is usually more ressource efficient - compared to Full virtualization
    """)

with st.expander("Docker"):
    st.image("app/static/docker_architecture.webp", caption="Docker Architecture", use_container_width=True)
    st.markdown("""
    - Docker is a collection of tools for managing images and running containers
    - The part of Docker, which hosts your containers is called the **Docker Engine**
    """)

st.subheader("Dev Containers")

with st.expander("Architecture"):
    st.image(
        "app/static/architecture_devcontainers.png",
        caption="Dev Containers Architecture",
        use_container_width=True,
    )

with st.expander("Advantages"):
    st.markdown(
        """
    - Clean capsulation of concerns and environments
    - Easy to setup
    - Documentation of installed dependencies and there respective versions
    """
    )

column_one, _, column_two = st.columns([3, 5, 2])

with column_one:
    st.page_link(
        "pages/1_Prerequisites.py",
        label="Previous: Prerequisites",
        use_container_width=True,
    )

with column_two:
    st.page_link(
        "pages/3_Workshop.py", label="Next: Workshop", use_container_width=True
    )
