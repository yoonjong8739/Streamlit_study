import streamlit as st

if "TDL" not in st.session_state:
    st.session_state["TDL"] = []

doit = st.text_input("할 일")
duedate = st.date_input("마감 기한")

button_clicked = st.button("추가하기")

if button_clicked:
    st.session_state["TDL"].append({"할 일": doit, "마감 기한": duedate})
    st.rerun()

st.data_editor(st.session_state["TDL"])