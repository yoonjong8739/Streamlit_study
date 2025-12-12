import streamlit as st

def calulate_grade(score):
    if score >= 70:
        return 'A'
    elif score >= 60:
        return 'B'
    elif score >= 50:
        return 'C'
    else:
        return 'F'

data = {}
with st.form("학점 계산기"):
    data["name"] = st.text_input("이름")
    data["score"] = st.number_input("점수", min_value=0, max_value=100, step=1)
    data["grade"] = calulate_grade(data["score"])
    
    #name = st.text_input("이름")
    #score = st.number_input("점수", min_value=0, max_value=100, step=1)
    st.form_submit_button("제출")

st.table(data)

#st.table({
#    "name" : name,
#    "score" : score,
#    "grade" : calulate_grade(score)
#})