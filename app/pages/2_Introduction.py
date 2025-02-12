import streamlit as st


st.set_page_config(
    page_title=f"{st.session_state.page_title} - Introduction",
    page_icon=st.session_state.page_icon
)


# page content
st.header("Introduction")


# first_slide =  st.expander("Virtualization")
# second_slide =  st.expander("Containerization")
# third_slide = st.expander("Dev Containers")

st.subheader("Virtualization")

with st.expander("Terminology"):
    st.markdown(
        "- **Host**: Computer used to virtualize\n"
        "- **Guest**: Virtual machine\n"
    )

with st.expander("Hardware Level Virtualization"):
    st.text("CONTENT")

with st.expander("Software Level Virtualization"):
    st.text("CONTENT")

with st.expander("OS Level Virtualization"):
    st.text("CONTENT")

st.subheader("Containerization")

st.subheader("Dev Containers")
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