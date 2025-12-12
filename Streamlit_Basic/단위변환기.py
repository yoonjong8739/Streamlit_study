import streamlit as st

st.image("./streamlit_study/img/ruler.png")
st.title("단위 변환기")
st.subheader("길이")

centimeter = 10.00
input_int = st.number_input(
    label="cm",
    value=centimeter,
    format="%.2f",
    placeholder="숫자를 입력하세요..."
)

st.subheader("바꿀 단위")
trans_type = st.selectbox("단위", options=["mm", "inch"])  # 드롭다운 메뉴
trans_click = st.button("변환하기")

st.subheader("바꾼 길이")
if trans_type == "mm" and trans_click:
    st.write(f"{input_int*10} mm")
elif trans_type == "inch" and trans_click:
    st.write(f"{input_int*0.38} inch")