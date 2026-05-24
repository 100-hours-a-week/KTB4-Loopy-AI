from contextlib import asynccontextmanager
from fastapi import FastAPI

from database import Base, engine
from routes import diary_routes, comment_routes
from ai.emotion_classifier import load_model, clear_model


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 서버 시작 시 감정 분류 모델 로드
    load_model()
    yield
    # 서버 종료 시 정리
    clear_model()


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="오늘의 기분 API",
    description="AI 감정 분류 기반 익명 일기 커뮤니티",
    lifespan=lifespan,
)

app.include_router(diary_routes.router)
app.include_router(comment_routes.router)


@app.get("/")
def root():
    return {"message": "🌈 오늘의 기분 API에 오신 것을 환영합니다"}
