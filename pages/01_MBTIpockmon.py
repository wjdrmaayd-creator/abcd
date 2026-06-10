import streamlit as st

st.set_page_config(page_title="MBTI 포켓몬 추천", page_icon="🎮")

st.title("🎮 MBTI 포켓몬 캐릭터 추천")
st.write("MBTI를 선택하면 나와 닮은 포켓몬 캐릭터와 성격을 알려줘요!")

pokemon_data = {
    "INTJ": {
        "pokemon": "뮤츠",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/150.png",
        "personality": "차분하고 강한 카리스마가 있어요. 깊이 생각하고 전략적으로 움직이는 타입이며, 목표가 생기면 끝까지 집중해 해내요."
    },
    "INTP": {
        "pokemon": "메타몽",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png",
        "personality": "호기심이 많고 상상력이 풍부해요. 정해진 틀보다 새로운 방식으로 생각하는 걸 좋아해요."
    },
    "ENTJ": {
        "pokemon": "리자몽",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/6.png",
        "personality": "강한 리더십과 추진력을 가진 타입이에요. 목표를 향해 자신감 있게 나아가요."
    },
    "ENTP": {
        "pokemon": "팬텀",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/94.png",
        "personality": "창의적이고 재치가 넘쳐요. 새로운 아이디어를 내고 도전하는 것을 좋아해요."
    },
    "INFJ": {
        "pokemon": "루기아",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/249.png",
        "personality": "통찰력이 뛰어나고 배려심이 많아요. 주변 사람들을 잘 이해하는 타입이에요."
    },
    "INFP": {
        "pokemon": "이브이",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/133.png",
        "personality": "따뜻한 감성과 풍부한 상상력을 가지고 있어요."
    },
    "ENFJ": {
        "pokemon": "피카츄",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png",
        "personality": "사람들과 어울리는 것을 좋아하고 긍정적인 에너지가 넘쳐요."
    },
    "ENFP": {
        "pokemon": "뮤",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/151.png",
        "personality": "자유롭고 창의적이며 새로운 경험을 즐겨요."
    },
    "ISTJ": {
        "pokemon": "거북왕",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/9.png",
        "personality": "책임감이 강하고 신뢰할 수 있는 타입이에요."
    },
    "ISFJ": {
        "pokemon": "해피너스",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/242.png",
        "personality": "친절하고 배려심이 많아 주변 사람들을 잘 챙겨요."
    },
    "ESTJ": {
        "pokemon": "보스로라",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/306.png",
        "personality": "체계적이고 결단력이 뛰어난 리더형이에요."
    },
    "ESFJ": {
        "pokemon": "푸크린",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/40.png",
        "personality": "사교적이고 협동심이 강해요."
    },
    "ISTP": {
        "pokemon": "한카리아스",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/445.png",
        "personality": "실용적이며 문제 해결 능력이 뛰어나요."
    },
    "ISFP": {
        "pokemon": "나인테일",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/38.png",
        "personality": "감수성이 풍부하고 예술적인 감각을 지녔어요."
    },
    "ESTP": {
        "pokemon": "괴력몬",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/68.png",
        "personality": "활동적이고 도전을 즐기는 타입이에요."
    },
    "ESFP": {
        "pokemon": "꼬부기",
        "image": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png",
        "personality": "밝고 유쾌하며 사람들과 함께하는 것을 좋아해요."
    }
}

mbti = st.selectbox(
    "MBTI를 선택하세요",
    list(pokemon_data.keys())
)

selected = pokemon_data[mbti]

st.markdown("---")

st.subheader(f"✨ {selected['pokemon']}")

st.image(
    selected["image"],
    width=250
)

st.write(selected["personality"])
