
import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 추천",
    page_icon="🚀"
)

st.title("🚀 MBTI 진로 추천기")

career_data = {
    "INTJ": [
        {
            "career": "🧠 AI 연구원",
            "major": "인공지능학과, 컴퓨터공학과",
            "personality": "논리적이고 전략적으로 생각하는 사람"
        },
        {
            "career": "📊 데이터 과학자",
            "major": "통계학과, 데이터사이언스학과",
            "personality": "분석을 좋아하는 사람"
        }
    ],

    "INTP": [
        {
            "career": "💻 소프트웨어 개발자",
            "major": "컴퓨터공학과",
            "personality": "호기심이 많고 탐구를 좋아하는 사람"
        },
        {
            "career": "🔬 연구원",
            "major": "물리학과, 화학과",
            "personality": "깊게 생각하는 사람"
        }
    ],

    "ENTJ": [
        {
            "career": "🏢 CEO",
            "major": "경영학과",
            "personality": "리더십이 강한 사람"
        },
        {
            "career": "📈 경영 컨설턴트",
            "major": "경제학과",
            "personality": "문제 해결을 좋아하는 사람"
        }
    ],

    "ENTP": [
        {
            "career": "🚀 창업가",
            "major": "창업학과",
            "personality": "도전을 즐기는 사람"
        },
        {
            "career": "📢 마케팅 기획자",
            "major": "광고홍보학과",
            "personality": "창의적인 사람"
        }
    ],

    "INFJ": [
        {
            "career": "🩺 심리상담사",
            "major": "심리학과",
            "personality": "공감 능력이 뛰어난 사람"
        },
        {
            "career": "✍️ 작가",
            "major": "문예창작과",
            "personality": "상상력이 풍부한 사람"
        }
    ],

    "INFP": [
        {
            "career": "🎨 일러스트레이터",
            "major": "시각디자인학과",
            "personality": "감수성이 풍부한 사람"
        },
        {
            "career": "🎬 콘텐츠 크리에이터",
            "major": "미디어학과",
            "personality": "개성이 강한 사람"
        }
    ],

    "ENFJ": [
        {
            "career": "👩‍🏫 교사",
            "major": "교육학과",
            "personality": "사람을 돕는 것을 좋아하는 사람"
        },
        {
            "career": "🤝 인사담당자",
            "major": "경영학과",
            "personality": "소통 능력이 좋은 사람"
        }
    ],

    "ENFP": [
        {
            "career": "🎤 방송인",
            "major": "방송연예학과",
            "personality": "에너지가 넘치는 사람"
        },
        {
            "career": "📱 SNS 마케터",
            "major": "미디어학과",
            "personality": "트렌드를 좋아하는 사람"
        }
    ],

    "ISTJ": [
        {
            "career": "⚖️ 공무원",
            "major": "행정학과",
            "personality": "책임감이 강한 사람"
        },
        {
            "career": "💰 회계사",
            "major": "회계학과",
            "personality": "꼼꼼한 사람"
        }
    ],

    "ISFJ": [
        {
            "career": "🏥 간호사",
            "major": "간호학과",
            "personality": "배려심이 많은 사람"
        },
        {
            "career": "👶 유치원 교사",
            "major": "유아교육과",
            "personality": "아이들을 좋아하는 사람"
        }
    ],

    "ESTJ": [
        {
            "career": "🏛️ 행정 관리자",
            "major": "행정학과",
            "personality": "체계적인 사람"
        },
        {
            "career": "📋 프로젝트 매니저",
            "major": "경영학과",
            "personality": "계획을 잘 세우는 사람"
        }
    ],

    "ESFJ": [
        {
            "career": "🎓 진로상담사",
            "major": "심리학과",
            "personality": "친절한 사람"
        },
        {
            "career": "🏨 호텔리어",
            "major": "호텔관광학과",
            "personality": "서비스 정신이 좋은 사람"
        }
    ],

    "ISTP": [
        {
            "career": "🔧 기계 엔지니어",
            "major": "기계공학과",
            "personality": "실용적인 사람"
        },
        {
            "career": "✈️ 항공정비사",
            "major": "항공정비학과",
            "personality": "기계를 좋아하는 사람"
        }
    ],

    "ISFP": [
        {
            "career": "📸 사진작가",
            "major": "사진영상학과",
            "personality": "예술 감각이 뛰어난 사람"
        },
        {
            "career": "🎨 디자이너",
            "major": "디자인학과",
            "personality": "창의적인 사람"
        }
    ],

    "ESTP": [
        {
            "career": "⚽ 스포츠 마케터",
            "major": "스포츠산업학과",
            "personality": "활동적인 사람"
        },
        {
            "career": "💼 영업 전문가",
            "major": "경영학과",
            "personality": "사람 만나는 것을 좋아하는 사람"
        }
    ],

    "ESFP": [
        {
            "career": "🎭 배우",
            "major": "연극영화학과",
            "personality": "표현력이 풍부한 사람"
        },
        {
            "career": "🎉 이벤트 기획자",
            "major": "관광경영학과",
            "personality": "즐거운 분위기를 좋아하는 사람"
        }
    ]
}

mbti = st.selectbox(
    "✨ MBTI를 선택하세요!",
    list(career_data.keys())
)

if st.button("🔍 진로 추천 보기"):
    st.success(f"{mbti} 유형 추천 결과!")

    for item in career_data[mbti]:
        st.subheader(item["career"])
        st.write("🎓 추천 학과:", item["major"])
        st.write("😎 잘 맞는 성격:", item["personality"])
        st.divider()

st.caption("💡 MBTI는 참고용이야! 가장 중요한 건 네가 좋아하는 일을 찾는 거야 😊")
