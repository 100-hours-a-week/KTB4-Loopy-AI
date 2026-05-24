from datetime import datetime

from pydantic import BaseModel


class DiaryIn(BaseModel):
    content: str


class DiaryOut(BaseModel):
    id: int
    content: str
    emotion: str
    created_at: datetime

    class Config:
        from_attributes = True
