import streamlit as st
from streamlit_calendar import calendar

st.set_page_config(page_title="Demo for streamlit-calendar", page_icon="📆")

mode = st.selectbox(
    "Calendar Mode:",
    (
        "daygrid",
        "resource-daygrid",
        "list",
        "multimonth",
    ),
)

with st.form("Calendar Mode"):
    title_event1 = st.text_input("Event Title")
    color = st.selectbox("Choose Color:", ("red",
                                           "yellow",
                                           "orange",
                                           "green",
                                           "blue",
                                           "brown"))
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    resourceId = st.selectbox("Resource Id:", ("a", "b", "c"))

    submit = st.form_submit_button("Submit")

if "events" not in st.session_state:
    st.session_state.events = [
        # ... Gán dữ liệu cứng
    ]

if submit:
    new_event = {
        "title": title_event1,
        "color": color,
        "start": f"{start_date}",
        "end": f"{end_date}",
        "resourceId": resourceId,
    }
    st.session_state.events.append(new_event)

    st.snow()  # Successfully

calendar_resources = [
    {"id": "a", "building": "Building A", "title": "Room A"},
    {"id": "b", "building": "Building A", "title": "Room B"},
    {"id": "c", "building": "Building B", "title": "Room C"},
    {"id": "d", "building": "Building B", "title": "Room D"},
    {"id": "e", "building": "Building C", "title": "Room E"},
    {"id": "f", "building": "Building C", "title": "Room F"},
]

calendar_options = {
    "editable": "true",
    "navLinks": "true",
    "resources": calendar_resources,
    "selectable": "true",
}

if "resource" in mode:
    if mode == "resource-daygrid":
        calendar_options.update({
            "initialDate": "2023-07-01",
            "initialView": "resourceDayGridDay",
            "resourceGroupField": "building",
        })
else:
    if mode == "daygrid":
        calendar_options.update({
            "headerToolbar": {
                "left": "today prev,next",
                "center": "title",
                "right": "dayGridDay,dayGridWeek,dayGridMonth",
            },
            "initialDate": "2023-07-01",
            "initialView": "dayGridMonth",
        })
    elif mode == "timeline":
        calendar_options.update({
            "headerToolbar": {
                "left": "today prev,next",
                "center": "title",
                "right": "timelineWeek,timelineMonth",
            },
            "initialDate": "2023-07-01",
            "initialView": "timelineMonth",
        })
    elif mode == "list":
        calendar_options.update({
            "initialDate": "2023-07-01",
            "initialView": "listMonth",
        })
    elif mode == "multimonth":
        calendar_options.update({
            "initialView": "multiMonthYear",
        })

state = calendar(
    events=st.session_state.get("events", []),
    options=calendar_options,
    custom_css="""
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
    """,
    key=mode,
)