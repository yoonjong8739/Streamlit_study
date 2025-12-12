import streamlit as st

ZODIAC_SIGNS = {
    "물병자리": {
        "start": [1, 20],
        "end": [2, 18]
    },
    "물고기자리": {
        "start": [2, 19],
        "end": [3, 20],
    },
    "양자리": {
        "start": [3, 21],
        "end": [4, 19],
    },
    "황소자리": {
        "start": [4, 20],
        "end": [5, 20],
    },
    "쌍둥이자리": {
        "start": [5, 21],
        "end": [6, 21],
    },
    "게자리": {
        "start": [6, 22],
        "end": [7, 22],
    },
    "사자자리": {
        "start": [7, 23],
        "end": [8, 22],
    },
    "처녀자리": {
        "start": [8, 23],
        "end": [9, 22],
    },
    "천칭자리": {
        "start": [9, 23],
        "end": [10, 22],
    },
    "전갈자리": {
        "start": [10, 23],
        "end": [11, 22],
    },
    "사수자리": {
        "start": [11, 23],
        "end": [12, 21],
    },
    "염소자리": {
        "start": [12, 22],
        "end": [1, 19],
    },
}

def get_zodiac(month, day):
    for key in ZODIAC_SIGNS:
        sign = ZODIAC_SIGNS[key]
        if (month == sign["start"][0] and day >= sign["start"][1]) or (month == sign["end"][0] and day <= sign["end"][1]):
            return key
    return None

st.title("내 별자리 찾기")

birth_date = st.date_input("생년월일을 선택하세요")
zodiac = get_zodiac(birth_date.month, birth_date.day)

st.subheader("당신의 별자리는...")
st.header(zodiac)
