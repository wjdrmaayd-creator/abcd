import streamlit as st

st.title("🎮 MBTI 포켓몬 추천")

pokemon_mbti = {
    "INTJ": {
        "name": "뮤츠",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/150.png"
    },
    "INTP": {
        "name": "후딘",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/065.png"
    },
    "ENTJ": {
        "name": "리자몽",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/006.png"
    },
    "ENFP": {
        "name": "피카츄",
        "image": "https://assets.pokemon.com/assets/cms2/img/pokedex/full/025.png"
    }
}

mbti = st.selectbox(
    "MBTI를 선택하세요",
    list(pokemon_mbti.keys())
)

pokemon = pokemon_mbti[mbti]

col1, col2 = st.columns([1, 2])

with col1:
    st.image(pokemon["image"], width=250)

with col2:
    st.subheader(f"추천 포켓몬: {pokemon['name']}")
    st.write(f"{mbti} 유형에게 어울리는 포켓몬입니다.")
