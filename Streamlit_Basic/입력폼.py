import streamlit as st

# st.form()
# 폼은 인풋들을 모아 놓고 쓰면서 폼의 제출 버튼을 눌렀을 때만 rerun이 되도록 해 주는 기능
# 모든 값을 입력 받고 나서 코드를 실행하고 싶을 때 사용

# 폼 제출 버튼 - st.form_submit_button()
# 일반적인 버튼은 폼 안에 배치 불가

data = {}

with st.form("과목 설문 조사"):
    data["date"] = st.date_input("수강 날짜")
    data["name"] = st.text_input("이름")
    data["description"] = st.text_area("전체 소감")
    data["level"] = st.number_input(label="학년", value=1, step=1)
    data["preference"] = st.slider(label="과목 선호도", min_value=1, max_value=10, step=1)
    data["difficulty"] = st.radio(label="난이도", options=["쉬움", "보통", "어려움"])
    data["is_retaking"] = st.checkbox(label="재수강 여부")
    
    st.form_submit_button("적용")

st.table(data)