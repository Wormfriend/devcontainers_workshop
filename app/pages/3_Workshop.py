from datetime import datetime, timezone
import streamlit as st


def timer(days: int=10, hours: int=10, minutes: int=10, seconds: int=10) -> str:
    html: str = """<div style="display: flex; gap: 10px;">
        <h1 style="color: red;">Text</h1>
        <h1 style="color: red;">Text</h1>
        <h1 style="color: red;">Text</h1>
    </div>"""

    return html

st.set_page_config(
    page_title=f"{st.session_state.page_title} - Workshop",
    page_icon=st.session_state.page_icon
)
# st.html(
#     "<style>"
#     """
#         st-key-timer {
#             font-size: 100px;
#         }
#     """
#     "</style>"
# )

st.header("Workshop")

st.html(timer())
# time_now = datetime.now(tz=timezone.utc)
# time_activation = datetime(2025, 2, 13, tzinfo=timezone.utc)

# if time_now < time_activation:
#     delta = time_activation - time_now

st.subheader("Workshop available in:")



# else:
with st.expander("Create A Dockerfile"):
    st.write("YOUR TEXT HERE")

with st.expander("Create A devcontainer.json"):
    st.write("YOUR TEXT HERE")

with st.expander("Add your favourite extensions"):
    st.write("YOUR TEXT HERE")

with st.expander("Create requirements.txt"):
    st.write("YOUR TEXT HERE")

with st.expander("Start your devcontainer"):
    st.write("YOUR TEXT HERE")

with st.expander("Clone Git-Repository"):
    st.write("YOUR TEXT HERE")


# footer
column_one, _, column_two = st.columns([3, 4, 2])

with column_one:
    st.page_link("pages/2_Introduction.py", label="Previous: Introduction", use_container_width=True)

with column_two:
    st.page_link("pages/4_Ressources.py", label="Next: Ressources", use_container_width=True)
