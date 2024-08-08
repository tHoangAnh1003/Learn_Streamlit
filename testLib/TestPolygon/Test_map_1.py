import streamlit as st
import leafmap.foliumap as leafmap
import json
import folium
from PIL import Image
import io
import requests
from PIL import ImageDraw


def handle_map_click(e):
    if 'points' not in st.session_state:
        st.session_state.points = []
    if len(st.session_state.points) < 4:
        st.session_state.points.append((e['latlng']['lat'], e['latlng']['lng']))
        st.session_state.map.add_child(folium.Marker(location=[e['latlng']['lat'], e['latlng']['lng']]))


m = leafmap.Map(center=[21.0285, 105.8542], zoom=12)

m.add_event_listener('click', handle_map_click)

st.title("Chọn 4 điểm trên bản đồ")
st.write("Nhấn vào bản đồ để chọn 4 điểm.")
st.markdown(m.to_html(), unsafe_allow_html=True)

if 'points' in st.session_state and len(st.session_state.points) == 4:
    points_json = json.dumps(st.session_state.points)
    st.write("Tọa độ 4 điểm đã chọn:")
    st.json(points_json)

    m.save('map.html')
    img_url = "http://localhost:8501/map.html"
    img_data = requests.get(img_url).content
    img = Image.open(io.BytesIO(img_data))

    draw = ImageDraw.Draw(img)
    poly_coords = [(x[1], x[0]) for x in st.session_state.points]
    draw.polygon(poly_coords, outline='red', width=5)

    st.image(img, caption="Ảnh vùng chọn trên bản đồ")

    img.save("selected_area.png")
else:
    st.write("Vui lòng chọn 4 điểm.")
