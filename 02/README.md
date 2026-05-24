# [과제 2]
1. HTTP 내용 정리
2. FastAPI로 커뮤니티 서비스의 백엔드를 구현해보세요
    - HTTP REST API 설계 및 구현
    - AI 모델 서빙
    - 데이터베이스 적용하기
    - 구조 개선하기(예: Route - Controller - Model 패턴을 적용)
    - (선택) HTML/CSS/JS나 스트림릿으로 프론트엔드 만들기

## 📖 과제 내용
1. **HTTP 내용 정리**
2. **감정 일기 커뮤니티 "오늘의 기분"**
   - HTTP REST API 설계 및 구현
   - AI 감정 분류 모델 서빙
   - SQLite + SQLAlchemy 데이터베이스 적용
   - Route - Controller - Model 패턴 적용
  
## 🤖 AI 감정 분류
서버 시작 시 HuggingFace 감정 분류 모델을 **메모리에 한 번만 로드**합니다 (`lifespan` 활용).
일기 작성 시 AI가 텍스트를 분석하여 감정 태그를 자동 부여합니다.
```
[입력] "오늘 시험 망쳐서 너무 우울하다..."
[출력] 감정 태그: 슬픔 😢
```

## 📝 회고 (Review)
    
