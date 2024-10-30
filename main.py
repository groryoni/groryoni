import streamlit as st
st.title("함께 배우고 성장하는 사회시간🌏")
st.header("퇴근하고 싶다")

import streamlit as st
이름 = st.text_input("이름을 입력하세요.")
st.write(f"{이름}님 퇴근하세요.")

st.subheader("Subheader")
st.write("Hello **World**!!!")
st.markdown(":blue[헬로우] 월드!!!")

버튼 = st.button("눌러봐")
if 버튼:
    st.write("누르지 마.")

붕어빵 = st.checkbox("붕어빵(500원)")
군밤 = st.checkbox("군밤(3000원)")
고구마말랭이 = st.checkbox("고구마말랭이(2500원)")
가격 = 0
if 붕어빵:
    st.write("붕어빵을 선택하였습니다")
    가격 += 500
if 군밤:
    st.write("군밤을 선택하였습니다")
    가격 += 3000
if 고구마말랭이:
    st.write("고구마말랭이를 선택하였습니다")
    가격 += 2500
st.subheader(f"선택한 음식의 가격은 {가격}입니다")
import streamlit as st

result = st.radio("붕어빵은 팥붕이다.", ["O", "X"])
if result == "O":
    st.success("정답!!")
else:
    st.error("오답!!")

과목 = st.selectbox("과목을 선택하세요",
                    ["세계시민과 지리",
                     "한국지리 탐구",
                     "도시의 미래 탐구",
                     "여행지리"
                     "기후변화와 지속가능한 세계"])
st.subheader(f"당신이 선택한 과목은 {과목}입니다.")
