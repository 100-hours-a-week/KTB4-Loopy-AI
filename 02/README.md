# [과제 2]
1. HTTP 내용 정리
2. FastAPI로 커뮤니티 서비스의 백엔드를 구현해보세요
    1. HTTP REST API 설계 및 구현
    2. AI 모델 서빙
    3. 데이터베이스 적용하기
    4. 구조 개선하기(예: Route - Controller - Model 패턴을 적용)
    5. (선택) HTML/CSS/JS나 스트림릿으로 프론트엔드 만들기

## 📖 프로젝트 구조

fastapi_community/
├── README.md
├── .gitignore
├── requirements.txt
├── main.py
├── database.py
├── models/
│   ├── __init__.py
│   ├── post.py
│   └── comment.py
├── schemas/
│   ├── __init__.py
│   └── post.py
├── controllers/
│   ├── __init__.py
│   └── post_controller.py
├── routes/
    ├── __init__.py
    └── post_routes.py
├── main.py
├── database.py    # engine, db 생성
├── models.py      # sqlalchemy 테이블과 매핑
├── schemas.py     # pydantic validation
├── routers
│   ├── comments.py
│   ├── posts.py
│   └── users.py
├── services
│   ├── comments.py
│   ├── posts.py
│   ├── users.py
│   └── ai_service.py
├── repositories
│   ├── comments.py
│   ├── posts.py
│   └── users.py
└── README.md

## 📝 회고 (Review)
    
