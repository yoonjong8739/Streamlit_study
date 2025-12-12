# json 모듈을 사용하면 json 파일을 dictionary 형태로 변환하거나, 반대로 dictionary 형태를 json 파일로 변환할 수 있습니다.
# json.load()를 사용하면 파일에서 json 데이터를 읽어와 dictionary 형태로 변환할 수 있습니다.
# json.dump()를 사용하면 dictionary 형태의 데이터를 json 파일로 저장할 수 있습니다.

import json
import os
import streamlit as st

#def load_data1(filename):
#    data = None
#    with open(filename, "r", encoding="utf-8") as file:
#        data = json.load(file)
#    return data

#def save_data1(filename, data):
#    with open(filename, "w", encoding="utf-8") as file:
#        json.dump(data, file, indent=4, ensure_ascii=False)

# (참고) 파일이 없는 경우 처리하기
def load_data2(filename):
    data = None
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}  # 또는 [] 등 기본값 설정
    return data

def save_data2(filename, data):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving data to {filename}: {e}")

# Streamlit으로 일기 데이터 불러오기
if __name__ == "__main__":
    diary_dir = "./data.json"
    diary = load_data2(diary_dir)
    st.title("일기장")
    st.write(diary)