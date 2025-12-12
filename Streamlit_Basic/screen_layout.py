import streamlit as st

#col1, col2, col3 = st.columns(3)  # 3개 컬럼 생성
#col1, col2, col3 = st.columns([1, 2, 3])  # 컬럼 너비 비율(1:2:3)
#col1.write("column 1")
#col2.write("column 2")
#col3.write("column 3")

# with 문법 사용
# 1. column
col1, col2, col3 = st.columns(3)
with col1:
    st.header("제목")
    st.text("column 1")

with col2:
    st.header("제목2")
    st.text("column 2")
    st.button("확인")

with col3:
    st.header("제목3")

# 2. Tab
tab1, tab2, tab3 = st.tabs(["Pthon", "Streamlit", "Pandas"])
with tab1:
    st.header("Python")
    st.text("I ❤️ Python")
with tab2:
    st.header("Streamlit")
    st.text("I ❤️ Streamlit")
with tab3:
    st.header("Pandas")
    st.text("I ❤️ Pandas")

# 3. Sidebar
with st.sidebar:  # 사이드바는 독립적이라 코드의 위치는 상관없음!
    st.header("사이드바")
    st.text("사이드바 내용")
st.title("제목")
st.text("내용")