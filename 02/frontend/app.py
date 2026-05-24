"""Streamlit 프론트엔드 - 오늘의 기분."""

import requests
import streamlit as st

API_URL = "http://localhost:8000"

EMOTION_COLORS = {
    "기쁨": "🟡",
    "슬픔": "🔵",
    "분노": "🔴",
    "불안": "🟣",
    "평온": "🟢",
}

st.set_page_config(page_title="오늘의 기분", page_icon="🌈")
st.title("🌈 오늘의 기분")
st.caption("AI가 당신의 일기를 읽고 감정을 분석해드려요")

# 일기 작성
st.header("✍️ 오늘의 일기 쓰기")
with st.form("new_diary"):
    content = st.text_area("오늘 어떤 하루였나요?", height=150)
    submitted = st.form_submit_button("작성하기")

    if submitted and content.strip():
        res = requests.post(f"{API_URL}/diaries/", json={"content": content})
        if res.status_code == 201:
            diary = res.json()
            emoji = EMOTION_COLORS.get(diary["emotion"], "⚪")
            st.success(f"작성 완료! AI가 분석한 감정: {emoji} **{diary['emotion']}**")
            st.rerun()

# 감정별 필터
st.header("🔍 감정별 일기 보기")
selected = st.selectbox(
    "감정을 선택하세요",
    ["전체", "기쁨", "슬픔", "분노", "불안", "평온"],
)

if selected == "전체":
    diaries = requests.get(f"{API_URL}/diaries/").json()
else:
    diaries = requests.get(f"{API_URL}/diaries/emotions/{selected}").json()

# 일기 목록
for diary in diaries:
    emoji = EMOTION_COLORS.get(diary["emotion"], "⚪")
    with st.expander(f"{emoji} {diary['emotion']} - {diary['created_at'][:10]}"):
        st.write(diary["content"])
        if st.button("삭제", key=f"del_{diary['id']}"):
            requests.delete(f"{API_URL}/diaries/{diary['id']}")
            st.rerun()
