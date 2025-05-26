import streamlit as st
import pandas as pd
import pydeck as pdk

# 데이터 정의 (서울 주요 지점 예시)
data = pd.DataFrame({
    'lat': [37.5665, 37.5700, 37.5796],
    'lon': [126.9780, 126.9920, 126.9770],
    'place': ['시청', '동대문', '경복궁']
})

# pydeck으로 고급 지도 시각화
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',  # 지도 스타일
    initial_view_state=pdk.ViewState(
        latitude=37.5665,     # 초기 중심 위도
        longitude=126.9780,   # 초기 중심 경도
        zoom=11,              # 줌 레벨
        pitch=45              # 기울기
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=data,
            get_position='[lon, lat]',  # 열 이름 주의!
            get_color='[200, 30, 0, 160]',  # 빨간색 마커
            get_radius=300,  # 반경
            pickable=True,
        )
    ],
    tooltip={"text": "{place}"}
))


