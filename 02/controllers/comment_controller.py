from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.comment import Comment
from models.diary import Diary
from schemas.comment_schema import CommentIn


def create_comment(db: Session, diary_id: int, comment_in: CommentIn):
    diary = db.query(Diary).filter(Diary.id == diary_id).first()
    if not diary:
        raise HTTPException(status_code=404, detail="일기를 찾을 수 없습니다")

    new_comment = Comment(content=comment_in.content, diary_id=diary_id)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment
