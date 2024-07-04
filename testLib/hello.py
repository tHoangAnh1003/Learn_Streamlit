import streamlit as st
import pandas as pd

dates = pd.date_range(start='2024-01-01', end='2024-12-31')

st.title('Danh sách các ngày từ 1/1/2024 đến 31/12/2024')

container = st.container()
container.markdown(
    """
    <style>
    .scroll-container {
        display: flex;
        overflow-x: auto;
        white-space: nowrap;
    }
    .date-button {
        display: inline-block;
        margin: 0 5px;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        cursor: pointer;
    }
    </style>
    <div class="scroll-container">
    """,
    unsafe_allow_html=True
)

cols = container.columns(len(dates))

for idx, date in enumerate(dates):
    if (cols[idx].button(date.strftime('%d.%m.%Y'))):
        st.session_state.selected_date = date.strftime('%d.%m.%Y')
        st.experimental_rerun()


container.markdown("</div>", unsafe_allow_html=True)

if 'selected_date' in st.session_state:
    selected_date = st.session_state.selected_date
    st.write(f"Ngày đã chọn: {selected_date}")

    st.write("Hộp thoại hiển thị thêm thông tin về ngày đã chọn.")

    with st.expander("Chi tiết ngày"):
        st.write(f"Thông tin chi tiết về ngày {selected_date}")
        st.write("Thêm nội dung bạn muốn hiển thị ở đây.")








