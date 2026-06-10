import streamlit as st

st.set_page_config(page_title="MBTI 포켓몬 추천", page_icon="⚡")

st.title("⚡ MBTI 포켓몬 추천기")
st.write("MBTI를 선택하면 어울리는 포켓몬과 성격을 알려드립니다!")

pokemon_mbti = {
    "INTJ": {
        "name": "뮤츠",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/150.png",
        "description": "전략적이고 독립적이며 높은 지능을 가진 타입입니다. 목표를 향해 체계적으로 움직이는 리더형입니다."
    },
    "INTP": {
        "name": "후딘",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/065.png",
        "description": "논리적이고 분석적인 성향을 가집니다. 지식 탐구와 문제 해결을 즐깁니다."
    },
    "ENTJ": {
        "name": "리자몽",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/006.png",
        "description": "카리스마와 추진력이 강하며 목표 달성을 위해 적극적으로 행동합니다."
    },
    "ENTP": {
        "name": "팬텀",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/094.png",
        "description": "창의적이고 재치가 넘치며 새로운 아이디어를 즐기는 혁신가입니다."
    },
    "INFJ": {
        "name": "루기아",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/249.png",
        "description": "통찰력이 뛰어나고 이상주의적이며 타인을 배려하는 성향입니다."
    },
    "INFP": {
        "name": "이브이",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/133.png",
        "description": "따뜻하고 상상력이 풍부하며 자신만의 가치관을 중요하게 생각합니다."
    },
    "ENFJ": {
        "name": "피카츄",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png",
        "description": "사교적이고 긍정적이며 주변 사람들에게 에너지를 전달합니다."
    },
    "ENFP": {
        "name": "뮤",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/151.png",
        "description": "자유롭고 호기심이 많으며 새로운 경험을 즐깁니다."
    },
    "ISTJ": {
        "name": "거북왕",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/009.png",
        "description": "책임감이 강하고 신뢰할 수 있는 현실주의자입니다."
    },
    "ISFJ": {
        "name": "해피너스",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/242.png",
        "description": "배려심이 많고 헌신적이며 주변 사람을 챙기는 것을 좋아합니다."
    },
    "ESTJ": {
        "name": "보스로라",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/306.png",
        "description": "조직적이고 결단력이 있으며 책임감 있는 관리자형입니다."
    },
    "ESFJ": {
        "name": "푸크린",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/040.png",
        "description": "친절하고 협력적이며 사람들과의 관계를 중요하게 생각합니다."
    },
    "ISTP": {
        "name": "한카리아스",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/445.png",
        "description": "실용적이고 도전 정신이 강하며 문제 해결 능력이 뛰어납니다."
    },
    "ISFP": {
        "name": "나인테일",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/038.png",
        "description": "감수성이 풍부하고 예술적인 감각을 지닌 평화주의자입니다."
    },
    "ESTP": {
        "name": "괴력몬",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/068.png",
        "description": "활동적이고 대담하며 즉흥적인 행동을 즐깁니다."
    },
    "ESFP": {
        "name": "꼬부기",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/007.png",
        "description": "유쾌하고 에너지가 넘치며 사람들과 함께하는 것을 좋아합니다."
    }
}

mbti = st.selectbox(
    "MBTI를 선택하세요",
    list(pokemon_mbti.keys())
)

if st.button("결과 보기"):
    result = pokemon_mbti[mbti]

    st.subheader(f"🌟 당신의 포켓몬은 {result['name']}!")
    st.image(result["image"], width=300)
    st.write("### 성격 특징")
    st.write(result["description"])

    st.success(f"{mbti} 유형에게 잘 어울리는 포켓몬은 {result['name']}입니다!")import streamlit as st

st.set_page_config(page_title="MBTI 포켓몬 추천", page_icon="⚡")

st.title("⚡ MBTI 포켓몬 추천기")
st.write("MBTI를 선택하면 어울리는 포켓몬과 성격을 알려드립니다!")

pokemon_mbti = {
    "INTJ": {
        "name": "뮤츠",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/150.png",
        "description": "전략적이고 독립적이며 높은 지능을 가진 타입입니다. 목표를 향해 체계적으로 움직이는 리더형입니다."
    },
    "INTP": {
        "name": "후딘",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/065.png",
        "description": "논리적이고 분석적인 성향을 가집니다. 지식 탐구와 문제 해결을 즐깁니다."
    },
    "ENTJ": {
        "name": "리자몽",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/006.png",
        "description": "카리스마와 추진력이 강하며 목표 달성을 위해 적극적으로 행동합니다."
    },
    "ENTP": {
        "name": "팬텀",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/094.png",
        "description": "창의적이고 재치가 넘치며 새로운 아이디어를 즐기는 혁신가입니다."
    },
    "INFJ": {
        "name": "루기아",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/249.png",
        "description": "통찰력이 뛰어나고 이상주의적이며 타인을 배려하는 성향입니다."
    },
    "INFP": {
        "name": "이브이",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/133.png",
        "description": "따뜻하고 상상력이 풍부하며 자신만의 가치관을 중요하게 생각합니다."
    },
    "ENFJ": {
        "name": "피카츄",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png",
        "description": "사교적이고 긍정적이며 주변 사람들에게 에너지를 전달합니다."
    },
    "ENFP": {
        "name": "뮤",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/151.png",
        "description": "자유롭고 호기심이 많으며 새로운 경험을 즐깁니다."
    },
    "ISTJ": {
        "name": "거북왕",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/009.png",
        "description": "책임감이 강하고 신뢰할 수 있는 현실주의자입니다."
    },
    "ISFJ": {
        "name": "해피너스",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/242.png",
        "description": "배려심이 많고 헌신적이며 주변 사람을 챙기는 것을 좋아합니다."
    },
    "ESTJ": {
        "name": "보스로라",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/306.png",
        "description": "조직적이고 결단력이 있으며 책임감 있는 관리자형입니다."
    },
    "ESFJ": {
        "name": "푸크린",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/040.png",
        "description": "친절하고 협력적이며 사람들과의 관계를 중요하게 생각합니다."
    },
    "ISTP": {
        "name": "한카리아스",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/445.png",
        "description": "실용적이고 도전 정신이 강하며 문제 해결 능력이 뛰어납니다."
    },
    "ISFP": {
        "name": "나인테일",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/038.png",
        "description": "감수성이 풍부하고 예술적인 감각을 지닌 평화주의자입니다."
    },
    "ESTP": {
        "name": "괴력몬",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/068.png",
        "description": "활동적이고 대담하며 즉흥적인 행동을 즐깁니다."
    },
    "ESFP": {
        "name": "꼬부기",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/007.png",
        "description": "유쾌하고 에너지가 넘치며 사람들과 함께하는 것을 좋아합니다."
    }
}

mbti = st.selectbox(
    "MBTI를 선택하세요",
    list(pokemon_mbti.keys())
)

if st.button("결과 보기"):
    result = pokemon_mbti[mbti]

    st.subheader(f"🌟 당신의 포켓몬은 {result['name']}!")
    st.image(result["image"], width=300)
    st.write("### 성격 특징")
    st.write(result["description"])

    st.success(f"{mbti} 유형에게 잘 어울리는 포켓몬은 {result['name']}입니다!")
