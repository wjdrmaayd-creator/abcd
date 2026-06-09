import streamlit as st

st.set_page_config(
page_title="MBTI 진로 추천",
page_icon="🚀",
layout="centered"
)

st.title("🚀 MBTI 진로 탐험대")
st.markdown("### 나의 MBTI에 딱 맞는 진로를 찾아보자! 😎")

career_data = {
"INTJ": [
{
"career": "🧠 AI 연구원",
"major": "인공지능학과, 컴퓨터공학과",
"personality": "논리적이고 미래를 내다보는 전략가형! 복잡한 문제를 해결하는 걸 좋아하는 친구에게 잘 맞아."
},
{
"career": "📊 데이터 과학자",
"major": "통계학과, 데이터사이언스학과",
"personality": "숫자와 분석을 좋아하고 체계적으로 생각하는 사람에게 추천!"
}
],
"INTP": [
{
"career": "💻 소프트웨어 개발자",
"major": "컴퓨터공학과",
"personality": "호기심이 많고 새로운 아이디어를 탐구하는 사람에게 딱!"
},
{
"career": "🔬 연구원",
"major": "물리학과, 화학과",
"personality": "깊이 있게 탐구하고 원리를 파헤치는 것을 좋아하는 친구에게 추천!"
}
],
"ENTJ": [
{
"career": "🏢 CEO",
"major": "경영학과",
"personality": "리더십이 강하고 목표를 향해 추진력 있게 나아가는 사람에게 잘 맞아."
},
{
"career": "📈 경영 컨설턴트",
"major": "경제학과, 경영학과",
"personality": "문제 해결 능력이 뛰어나고 조직을 이끄는 걸 좋아한다면 추천!"
}
],
"ENTP": [
{
"career": "🚀 스타트업 창업가",
"major": "경영학과, 창업학과",
"personality": "새로운 도전을 좋아하고 아이디어가 넘치는 친구에게 딱!"
},
{
"career": "📢 마케팅 기획자",
"major": "광고홍보학과",
"personality": "창의적이고 사람들과 소통하는 것을 좋아하는 사람에게 추천!"
}
],
"INFJ": [
{
"career": "🩺 심리상담사",
"major": "심리학과",
"personality": "공감 능력이 뛰어나고 다른 사람을 돕는 걸 좋아하는 친구에게 추천!"
},
{
"career": "✍️ 작가",
"major": "국문학과, 문예창작과",
"personality": "깊은 생각과 풍부한 상상력을 가진 사람에게 잘 맞아."
}
],
"INFP": [
{
"career": "🎨 일러스트레이터",
"major": "시각디자인학과",
"personality": "감수성이 풍부하고 창의적인 표현을 좋아하는 친구에게 추천!"
},
{
"career": "🎬 콘텐츠 크리에이터",
"major": "미디어학과",
"personality": "자신만의 개성을 표현하고 새로운 콘텐츠를 만드는 걸 좋아한다면 딱!"
}
],
"ENFJ": [
{
"career": "👩‍🏫 교사",
"major": "교육학과",
"personality": "사람들의 성장을 돕고 이끄는 것을 좋아하는 친구에게 추천!"
},
{
"career": "🤝 인사담당자",
"major": "경영학과",
"personality": "소통 능력이 뛰어나고 사람을 이해하는 데 강점이 있어."
}
],
"ENFP": [
{
"career": "🎤 방송인",
"major": "방송연예학과",
"personality": "에너지가 넘치고 사람들과 소통하는 것을 좋아하는 친구에게 딱!"
},
{
"career": "📱 SNS 마케터",
"major": "미디어학과",
"personality": "트렌드에 민감하고 창의적인 아이디어가 많은 사람에게 추천!"
}
],
"ISTJ": [
{
"career": "⚖️ 공무원",
"major": "행정학과",
"personality": "책임감이 강하고 꼼꼼한 사람에게 잘 맞아."
},
{
"career": "💰 회계사",
"major": "회계학과",
"personality": "정확성과 신뢰를 중요하게 생각하는 친구에게 추천!"
}
],
"ISFJ": [
{
"career": "🏥 간호사",
"major": "간호학과",
"personality": "배려심이 많고 다른 사람을 돕는 것을 좋아하는 사람에게 추천!"
},
{
"career": "👶 유치원 교사",
"major": "유아교육과",
"personality": "따뜻한 마음으로 아이들을 돌보는 데 보람을 느끼는 친구에게 잘 맞아."
}
],
"ESTJ": [
{
"career": "🏛️ 행정 관리자",
"major": "행정학과",
"personality": "체계적이고 조직을 이끄는 능력이 뛰어난 사람에게 추천!"
},
{
"career": "📋 프로젝트 매니저",
"major": "경영학과",
"personality": "계획을 세우고 실행하는 것을 좋아하는 친구에게 딱!"
}
],
"ESFJ": [
{
"career": "🎓 진로상담사",
"major": "교육학과, 심리학과",
"personality": "친절하고 사람들을 도와주는 걸 좋아하는 친구에게 추천!"
},
{
"career": "🏨 호텔리어",
"major": "호텔관광학과",
"personality": "서비스 정신이 뛰어나고 사람들과 어울리는 걸 좋아한다면 딱!"
}
],
"ISTP": [
{
"career": "🔧 기계 엔지니어",
"major": "기계공학과",
"personality": "직접 만들고 고치는 것을 좋아하는 친구에게 추천!"
},
{
"career": "✈️ 항공 정비사",
"major": "항공정비학과",
"personality": "실용적이고 문제 해결 능력이 뛰어난 사람에게 잘 맞아."
}
],
"ISFP": [
{
"career": "📸 사진작가",
"major": "사진영상학과",
"personality": "감각적이고 예술적인 표현을 좋아하는 친구에게 추천!"
},
{
"career": "🎨 디자이너",
"major": "디자인학과",
"personality": "창의성과 미적 감각이 뛰어난 사람에게 딱!"
}
],
"ESTP": [
{
"career": "⚽ 스포츠 마케터",
"major": "스포츠산업학과",
"personality": "활동적이고 도전을 즐기는 친구에게 추천!"
},
{
"career": "💼 영업 전문가",
"major": "경영학과",
"personality": "사람들과 소통하며 성과를 내는 걸 좋아하는 사람에게 잘 맞아."
}
],
"ESFP": [
{
"career": "🎭 배우",
"major": "연극영화학과",
"personality": "밝고 표현력이 풍부한 친구에게 추천!"
},
{
"career": "🎉 이벤트 기획자",
"major": "관광경영학과",
"personality": "사람들을 즐겁게 하고 특별한 경험을 만드는 걸 좋아한다면 딱!"
}
]
}

selected_mbti = st.selectbox(
"✨ MBTI를 선택해 주세요!",
list(career_data.keys())
)

if st.button("🔍 진로 추천 보기"):
st.success(f"{selected_mbti} 유형에게 추천하는 진로야! 🚀")

```
for idx, item in enumerate(career_data[selected_mbti], start=1):
    st.markdown(f"## {idx}. {item['career']}")
    st.markdown(f"**🎓 추천 학과** : {item['major']}")
    st.markdown(f"**😎 잘 맞는 성격** : {item['personality']}")
    st.markdown("---")
```

st.caption("💡 MBTI는 참고용이야! 가장 중요한 건 네가 좋아하고 잘하는 것을 찾는 거야 😊")
