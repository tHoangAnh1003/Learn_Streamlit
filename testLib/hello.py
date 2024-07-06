import streamlit as st
from streamlit_calendar import calendar
from datetime import datetime

st.set_page_config(page_title="Demo cho streamlit-calendar", page_icon="📆")

# Hàm để tạo sự kiện mới
def create_event():
    title_event1 = st.text_input("Tiêu đề sự kiện: ", key="title_event")
    color = st.selectbox("Chọn màu:", ("red", "yellow", "orange", "green", "blue", "brown"), key="color_event")
    start_date = st.date_input("Ngày bắt đầu: ", key="start_date_event", value=st.session_state["selected_date"])
    end_date = st.date_input("Ngày kết thúc: ", key="end_date_event", value=st.session_state["selected_date"])
    description = st.text_area("Mô tả: ", key="description_event")

    submit = st.button("Gửi", key="submit_event")

    if submit:
        new_event = {
            "title": title_event1,
            "color": color,
            "start": f"{start_date}",
            "end": f"{end_date}",
            "description": description,
        }
        st.session_state.events.append(new_event)
        st.snow()  # Hiệu ứng khi thêm sự kiện thành công

# Khởi tạo trạng thái session cho sự kiện
if "events" not in st.session_state:
    st.session_state.events = []

# Khởi tạo trạng thái session cho ngày được chọn
if "selected_date" not in st.session_state:
    st.session_state.selected_date = datetime.today().date()

# Hiển thị lịch
calendar_options = {
    "editable": "true",
    "navLinks": "true",
    "selectable": "true",
    "headerToolbar": {
        "left": "today prev,next",
        "center": "title",
        "right": "dayGridDay,dayGridWeek,dayGridMonth",
    },
    "initialDate": str(st.session_state.selected_date),
    "initialView": "dayGridMonth",
}

# Lấy trạng thái lịch để phát hiện ngày được click
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
    key="calendar"
)

# Xử lý khi ngày được click để thiết lập ngày được chọn
if state and "start" in state:
    st.session_state.selected_date = datetime.strptime(state["start"], "%Y-%m-%d").date()

# Hiển thị form để tạo sự kiện dựa trên ngày được chọn
st.write("### Tạo sự kiện")
create_event()
