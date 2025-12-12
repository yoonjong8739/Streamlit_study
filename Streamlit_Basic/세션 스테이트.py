import streamlit as st

if "number" not in st.session_state:
    st.session_state["number"] = 1
st.text(st.session_state["number"])

clicked = st.button("더하기")
if clicked:
    st.session_state["number"] += 1
    st.rerun()