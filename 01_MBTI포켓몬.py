import streamlit as st

st.title("MBTI & 포켓몬 선택")

mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

pokemon_list = [
    "피카츄", "리자몽", "이브이", "뮤츠",
    "팬텀", "루기아", "꼬부기", "이상해씨"
]

# 좌우 배치
col1, col2 = st.columns(2)

with col1:
    mbti = st.selectbox(
        "MBTI 선택",
        mbti_list
    )

with col2:
    pokemon = st.selectbox(
        "포켓몬 선택",
        pokemon_list
    )

st.divider()

st.write(f"선택한 MBTI : **{mbti}**")
st.write(f"선택한 포켓몬 : **{pokemon}**")

if st.button("결과 보기"):
    st.success(f"{mbti} 유형이 선택한 포켓몬은 {pokemon}입니다!")
