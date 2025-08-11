from sqlalchemy import Column, Integer, String, ForeignKey
from db import Base


class Information(Base):
    __tablename__ = 'information'
    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(255), nullable=False)
    example = Column(String(255), nullable=False)
    lesson_id = Column(Integer, ForeignKey('lesson.id'), nullable=False)