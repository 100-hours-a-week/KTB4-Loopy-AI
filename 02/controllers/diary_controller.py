from fastapi import HTTPException
from sqlalchemy.orm import Session

from ai.emotion_classifier import classify_emotion
from models.diary import Diary
from schemas.diary_schema import DiaryIn


def create_diary(db: Session, diary_in: DiaryIn):
    # AI로 감정 분류
    emotion = classify_emotion(diary_in.content)

    new_diary = Diary(content=diary_in.content, emotion=emotion)
    db.add(new_diary)
    db.commit()
    db.refresh(new_diary)
    return new_diary


def get_diaries(db: Session):
    return db.query(Diary).order_by(Diary.created_at.desc()).all()


def get_diary(db: Session, diary_id: int):
    diary = db.query(Diary).filter(Diary.id == diary_id).first()
    if not diary:
        raise HTTPException(status_code=404, detail="일기를 찾을 수 없습니다")
    return diary


def get_diaries_by_emotion(db: Session, emotion: str):
    return (
        db.query(Diary)
        .filter(Diary.emotion == emotion)
        .order_by(Diary.created_at.desc())
        .all()
    )


def delete_diary(db: Session, diary_id: int):
    diary = get_diary(db, diary_id)
    db.delete(diary)
    db.commit()
