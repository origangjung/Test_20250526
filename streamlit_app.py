import streamlit as st
import plotly.express as px
import pandas as pd

# 샘플 데이터
df = pd.DataFrame({
    "과일": ["사과", "바나나", "체리", "사과", "바나나", "체리"],
    "판매량": [10, 15, 8, 12, 18, 6],
    "지점": ["서울", "서울", "서울", "부산", "부산", "부산"]
})

# plotly 그래프 생성
fig = px.bar(df, x="과일", y="판매량", color="지점", barmode="group", title="과일별 판매량")

# Streamlit에 출력
st.plotly_chart(fig, use_container_width=True)

