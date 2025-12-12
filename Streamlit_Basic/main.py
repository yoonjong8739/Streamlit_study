import streamlit as st

st.write("# 안녕! Welcome to My Streamlit App")

name = "남윤종"
age = 30
date = "1996-04-15"

st.text_input("이름", name, placeholder="이름을 입력하세요")
st.number_input("나이", age)
st.date_input("생년월일", date)

st.write(3)
st.write("어서오세요")
st.write([
    "도윤",
    "하빈",
    "유하"
])
st.write({
    "아이스 커피": 4500,
    "카페 모카": 5000,
    "녹차": 5000
})
st.write([
    { "name": "아이스 커피", "price": 4500 },
    { "name": "카페모카", "price": 5000 },
    { "name": "녹차", "price": 5000 }
])

st.title("제목")
st.header("머릿말1")
st.subheader("작은 머릿말1")
st.text("본문1")
st.divider()
st.header("머릿말2")
st.subheader("작은 머릿말2")
st.text("본문2")
st.divider()

st.success("성공")
st.info("정보 전달")
st.warning("경고")
st.error("오류")

st.metric("오늘 날씨", "10°C", help="강원도 기준", delta=-2, border=True)

st.image("./streamlit_study/img/meerkat.jpg", width=200)
st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Meerkat_%28Suricata_suricatta%29_Tswalu.jpg/728px-Meerkat_%28Suricata_suricatta%29_Tswalu.jpg")
st.divider()

name = st.text_input("이름을 입력하세요")
st.write(f"안녕하세요, {name}님!")
st.divider()

st.title("과목 설문 조사")

date = st.date_input("수강 날짜")
name = st.text_input("이름")
description = st.text_area("수업에 대한 의견을 작성해주세요")

student_type = st.selectbox("교육과정", options=["중학생", "고등학생", "대학생"])  # 드롭다운 메뉴
level = st.number_input("학년", min_value=1, max_value=4, step=1)  # 숫자 입력
preference = st.slider("과목 선호도", min_value=1, max_value=10, step=1)  # 슬라이더
difficulty = st.radio("난이도", options=["쉬움", "보통", "어려움"])  # 라디오 버튼
is_retaking = st.checkbox("재수강 여부")  # 체크박스
st.divider()

date = st.date_input("날짜")
date_str1 = date.strftime("%Y-%m-%d")
date_str2 = date.strftime("%Y.%m.%d.")
st.divider()

clicked = st.button("확인")
st.write(clicked)
st.divider()

clicked_2 = st.button("확인 버튼")
if clicked_2:
    st.write("클릭함!")
st.divider()

st.link_button("코드잇에서 보기", "https://codeit.kr")
st.divider()

import streamlit as st

input_name = st.text_input("이름 입력")
clicked = st.button("인사하기")
if clicked:
    st.write(f"{input_name}님 안녕하세요!")
st.divider()

st.table([
    "도윤",
    "하빈",
    "유하"
])
st.table({
    "아이스 커피": 4500,
    "카페 모카": 5000,
    "녹차": 5000
})
st.table([
    {"메뉴": "아이스커피", "가격": 4500},
    {"메뉴": "카페 모카", "가격": 5000},
    {"메뉴": "녹차", "가격": 5000},
])
st.divider()

value1 = st.data_editor([
    "도윤",
    "하빈",
    "유하"
])
st.write(value1)

value2 = st.data_editor([
{ "메뉴": "아이스커피", "가격": 4500 },
{ "메뉴": "카페 모카", "가격": 5000 },
{ "메뉴": "녹차", "가격": 5000 },
])
st.write(value2)
st.divider()

data1 = [10, 25, 30, 40, 55]
st.bar_chart(data1, x_label="게임 시간", y_label="경험치")

data2 = [
    {
        "날짜": "2025-01",
        "경험치": 10,
        "특수 경험치": 2,
    },
    {
        "날짜": "2025-02",
        "경험치": 15,
        "특수 경험치": 4,
    },
    {
        "날짜": "2025-03",
        "경험치": 30,
        "특수 경험치": 10,
    },
    {
        "날짜": "2025-04",
        "경험치": 40,
        "특수 경험치": 15,
    }
]
st.bar_chart(data2, x="날짜", y=["경험치", "특수 경험치"], stack=True)
st.divider()

data1 = [10, 25, 30, 40, 55]
st.line_chart(data1, x_label="게임 시간", y_label="경험치")

data2 = [
    {
        "날짜": "2025-01",
        "경험치": 10,
        "체력": 100,
    },
    {
        "날짜": "2025-02",
        "경험치": 15,
        "체력": 200
    },
    {
        "날짜": "2025-03",
        "경험치": 30,
        "체력": 250,
    },
    {
        "날짜": "2025-04",
        "경험치": 40,
        "체력": 300,
    }
]
st.line_chart(data2, x="날짜", y=["경험치", "체력"])
st.divider()

