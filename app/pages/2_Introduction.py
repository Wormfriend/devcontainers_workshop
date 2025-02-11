import streamlit as st


st.set_page_config(
    page_title=f"{st.session_state.page_title} - Introduction",
    page_icon=st.session_state.page_icon
)


# page content
st.header("Introduction")

first_slide =  st.expander("Virtualization")
second_slide =  st.expander("Containerization")
third_slide = st.expander("Dev Containers")

with first_slide:
    st.write("Content")

    with st.expander("test"):
        st.write("test")

with second_slide:
    st.write("Content")

with third_slide:
    st.write("Content")


column_one, _, column_two = st.columns([3, 5, 2])

with column_one:
    st.page_link("pages/1_Prerequisites.py", label="Previous: Prerequisites", use_container_width=True)

with column_two:
    st.page_link("pages/3_Workshop.py", label="Next: Workshop", use_container_width=True)