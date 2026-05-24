"""AI 감정 분류 모듈.

서버 시작 시 모델을 메모리에 1회 로드하고,
일기 작성 시 텍스트의 감정을 분류한다.
"""

_model = None

EMOTION_LABELS = {
    "joy": "기쁨",
    "sadness": "슬픔",
    "anger": "분노",
    "fear": "불안",
    "neutral": "평온",
}


def load_model():
    """서버 시작 시 호출. 감정 분류 모델을 메모리에 로드."""
    global _model

    # 실제 HuggingFace 모델 사용 시 아래 주석 해제
    # from transformers import pipeline
    # _model = pipeline(
    #     "text-classification",
    #     model="j-hartmann/emotion-english-distilroberta-base",
    # )

    _model = "loaded"  # 데모용
    print("✅ 감정 분류 모델 로드 완료")


def clear_model():
    """서버 종료 시 호출."""
    global _model
    _model = None


def classify_emotion(text: str) -> str:
    """텍스트의 감정을 분류해 한글 태그로 반환."""
    if _model is None:
        return "평온"

    # 데모용 간단한 키워드 기반 분류
    if any(word in text for word in ["행복", "기쁨", "좋아", "최고", "신나"]):
        return "기쁨"
    if any(word in text for word in ["슬프", "우울", "눈물", "외로", "힘들"]):
        return "슬픔"
    if any(word in text for word in ["화나", "짜증", "열받", "분노"]):
        return "분노"
    if any(word in text for word in ["불안", "걱정", "두렵", "무서"]):
        return "불안"
    return "평온"

    # 실제 모델 사용 시:
    # result = _model(text)[0]
    # return EMOTION_LABELS.get(result["label"].lower(), "평온")
