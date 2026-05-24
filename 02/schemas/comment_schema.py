from datetime import datetime

from pydantic import BaseModel


class CommentIn(BaseModel):
    content: str


class CommentOut(BaseModel):
    id: int
    content: str
    diary_id: int
    created_at: datetime

    class Config:
        from_attributes = True
