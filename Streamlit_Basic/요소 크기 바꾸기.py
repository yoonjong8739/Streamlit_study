import streamlit as st

col1, col2 = st.columns(2)
with col1:
    value = st.data_editor([
    { "메뉴": "아이스커피", "가격": 4500 },
    { "메뉴": "카페 모카", "가격": 5000 },
    { "메뉴": "녹차", "가격": 5000 }
], width="stretch")  # 컨테이너에 해당하는 컬럼 영역에 꽉 차도록 너비를 늘려줌.

with col2:
    st.text("컬럼2")

st.text_area("내용1", height=100)
st.text_area("내용2", height=200)
st.text_area("내용3", height=300)