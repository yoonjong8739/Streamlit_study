import streamlit as st

st.title("간단 MBTI 검사")

mbti = []

energy = st.radio(label="에너지 방향", options=[
    "나는 외향적이다",
    "나는 내향적이다",
])
if energy == "나는 외향적이다":
    mbti.append("E")
else:
    mbti.append("I")

cognitive = st.radio(label="인식 기능", options=[
    "나는 감각으로 인식한다",
    "나는 직관적으로 인식한다",
])
if cognitive == "나는 감각으로 인식한다":
    mbti.append("S")
else:
    mbti.append("N")

judge = st.radio(label="판단 기능", options=[
    "나는 생각으로 판단한다",
    "나는 감정으로 판단한다",
])
if judge == "나는 생각으로 판단한다":
    mbti.append("T")
else:
    mbti.append("F")

life = st.radio(label="생활형", options=[
    "나는 즉흥적이다",
    "나는 계획적이다",
])
if life == "나는 즉흥적이다":
    mbti.append("P")
else:
    mbti.append("J")

clicked = st.button("결과 보기")
if clicked:
    st.subheader("당신의 MBTI는...")
    st.header("".join(mbti))
