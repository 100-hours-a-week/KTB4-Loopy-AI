from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from controllers import comment_controller
from database import get_db
from schemas.comment_schema import CommentIn, CommentOut

router = APIRouter(prefix="/diaries", tags=["comments"])


@router.post(
    "/{diary_id}/comments",
    response_model=CommentOut,
    status_code=status.HTTP_201_CREATED,
)
def create_comment(
    diary_id: int, comment: CommentIn, db: Session = Depends(get_db)
):
    return comment_controller.create_comment(db, diary_id, comment)
