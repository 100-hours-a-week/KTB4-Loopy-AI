from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Text
from sqlalchemy.orm import relationship

from database import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    diary_id = Column(Integer, ForeignKey("diaries.id"))
    created_at = Column(DateTime, default=datetime.utcnow)

    diary = relationship("Diary", back_populates="comments")
