# [과제 2]

## 📖 과제 내용

1. **HTTP 내용 정리**
2. **감정 일기 커뮤니티 "오늘의 기분"**
   - HTTP REST API 설계 및 구현
   - AI 감정 분류 모델 서빙
   - SQLite + SQLAlchemy 데이터베이스 적용
   - Route - Controller - Model 패턴 적용

## 🌈 오늘의 기분 - 감정 일기 커뮤니티

> 하루 일기를 올리면 AI가 감정을 자동 분류해서 태그를 달아주는 익명 커뮤니티 서비스

## 💡 프로젝트 소개

평범한 일기장도 좋지만, 비슷한 감정을 느낀 사람들의 글을 모아보면 어떨까?
"오늘의 기분"은 사용자가 익명으로 일기를 올리면 **AI가 자동으로 감정을 분석**하여
`기쁨` / `슬픔` / `분노` / `불안` / `평온` 같은 태그를 자동 부여합니다.

같은 감정 태그의 글을 모아 볼 수 있어, 공감과 위로를 나눌 수 있는 공간을 지향합니다.

## 🛠 기술 스택

- **Backend**: FastAPI, SQLAlchemy, Pydantic
- **Database**: SQLite
- **AI**: HuggingFace Transformers (한국어 감정 분류 모델)
- **Frontend**: Streamlit

## 📁 프로젝트 구조

```
mood_diary/
├── main.py                  # 앱 진입점
├── database.py              # DB 연결
├── models/                  # SQLAlchemy 테이블 정의
├── schemas/                 # Pydantic 입출력 스키마
├── controllers/             # 비즈니스 로직
├── routes/                  # URL 라우팅
├── ai/                      # 감정 분류 모델
└── frontend/                # Streamlit 화면
```

**Route - Controller - Model 패턴**으로 책임을 분리했습니다.

## 🚀 실행 방법

```bash
# 1. 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

# 2. 패키지 설치
pip install -r requirements.txt

# 3. 백엔드 서버 실행
uvicorn main:app --reload

# 4. (선택) 프론트엔드 실행
streamlit run frontend/app.py
```

- API 문서: http://localhost:8000/docs
- 프론트엔드: http://localhost:8501

## 📌 API 명세

| Method | Endpoint | 설명 |
|--------|----------|------|
| GET | `/diaries` | 일기 목록 조회 (감정 태그 필터 가능) |
| GET | `/diaries/{id}` | 일기 상세 조회 |
| POST | `/diaries` | 일기 작성 (AI 감정 자동 분류) |
| DELETE | `/diaries/{id}` | 일기 삭제 |
| POST | `/diaries/{id}/comments` | 댓글(공감/위로) 작성 |
| GET | `/diaries/emotions/{emotion}` | 특정 감정의 일기만 모아보기 |

## 🤖 AI 감정 분류

서버 시작 시 HuggingFace 감정 분류 모델을 **메모리에 한 번만 로드**합니다 (`lifespan` 활용).
일기 작성 시 AI가 텍스트를 분석하여 감정 태그를 자동 부여합니다.

```
[입력] "오늘 시험 망쳐서 너무 우울하다..."
[출력] 감정 태그: 슬픔 😢
```

## 🧠 학습 포인트

- REST API 설계 (URL은 자원, 메서드는 동작)
- Pydantic으로 입출력 자동 검증
- AI 모델 서빙 시 `lifespan` 이벤트 활용
- `Depends(get_db)`로 DB 세션 의존성 주입
- 계층 분리(Route → Controller → Model)로 유지보수성 확보

## 📝 회고 (Review)

### 👍 잘한 점
- HTTP의 기본 개념부터 차근차근 정리하고 시작해서, 단순히 따라 치는 게 아니라 "왜 이렇게 설계하는지"를 이해할 수 있었다.
- `main.py`에 모든 코드를 몰아넣지 않고 처음부터 Route - Controller - Model 패턴으로 분리해서, 기능을 추가할 때 어디를 수정해야 할지 명확했다.

### 😵 어려웠던 점
- FastAPI의 `Depends`, Pydantic의 `BaseModel`, SQLAlchemy의 ORM이 한꺼번에 등장해서 처음엔 각자의 역할이 헷갈렸다.
- AI 모델을 매 요청마다 로드하면 너무 느려진다는 것을 알게 됐고, `lifespan` 이벤트로 서버 시작 시 1회만 로드하도록 수정하는 과정에서 시행착오가 있었다.

### 💡 배운 점
- REST API는 단순히 URL을 만드는 게 아니라, "자원(URL) + 동작(HTTP 메서드)"의 조합으로 표현하는 설계 철학이라는 것을 이해했다.
- 계층 분리가 처음엔 귀찮게 느껴졌지만, 댓글 기능을 나중에 추가할 때 다른 코드를 거의 건드리지 않아도 돼서 그 가치를 체감했다.
- AI 모델 서빙은 단순히 모델을 호출하는 게 아니라, **로드 시점과 메모리 관리**가 중요하다는 것을 알게 됐다.

### 🚀 앞으로
- 사용자 인증(JWT) 기능을 붙여서 익명이 아닌 실제 회원제로 확장해보고 싶다.
- 한국어 감정 분류 모델(KoBERT 등)로 교체해서 더 정확한 분류 성능을 내보고 싶다.
- 테스트 코드(`pytest`)를 추가해서 리팩토링할 때 안전망을 만들고 싶다.
