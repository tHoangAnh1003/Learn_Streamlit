import streamlit as st
import leafmap.foliumap as lf
from streamlit_folium import st_folium

def app():
    st.title("Vẽ và Lấy Dữ Liệu Từ Bản Đồ")

    m = lf.Map(center=[21.0285, 105.8542], zoom=12, draw_export=True)
    m.add_basemap('SATELLITE')

    map_data = st_folium(m, height=600, width=800)

    if map_data is not None and map_data.get('last_active_drawing'):
        print("Tọa độ đối tượng cuối cùng đã vẽ:")
        print(map_data['last_active_drawing'])

    if map_data is not None and map_data.get('all_drawings'):
        print("Tất cả đối tượng đã vẽ:")
        print(map_data['all_drawings'])

app()
