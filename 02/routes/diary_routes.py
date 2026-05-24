from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from controllers import diary_controller
from database import get_db
from schemas.diary_schema import DiaryIn, DiaryOut

router = APIRouter(prefix="/diaries", tags=["diaries"])


@router.get("/", response_model=List[DiaryOut])
def get_diaries(db: Session = Depends(get_db)):
    return diary_controller.get_diaries(db)


@router.get("/{diary_id}", response_model=DiaryOut)
def get_diary(diary_id: int, db: Session = Depends(get_db)):
    return diary_controller.get_diary(db, diary_id)


@router.post("/", response_model=DiaryOut, status_code=status.HTTP_201_CREATED)
def create_diary(diary: DiaryIn, db: Session = Depends(get_db)):
    return diary_controller.create_diary(db, diary)


@router.delete("/{diary_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_diary(diary_id: int, db: Session = Depends(get_db)):
    diary_controller.delete_diary(db, diary_id)


@router.get("/emotions/{emotion}", response_model=List[DiaryOut])
def get_by_emotion(emotion: str, db: Session = Depends(get_db)):
    return diary_controller.get_diaries_by_emotion(db, emotion)
