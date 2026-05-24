from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.orm import relationship

from database import Base


class Diary(Base):
    __tablename__ = "diaries"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text, nullable=False)
    emotion = Column(String(20), nullable=False, index=True)  # AI가 자동 부여
    created_at = Column(DateTime, default=datetime.utcnow)

    comments = relationship(
        "Comment", back_populates="diary", cascade="all, delete-orphan"
    )
