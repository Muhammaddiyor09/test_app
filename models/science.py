from sqlalchemy import Column, Integer, String
from db import Base


class Science(Base):
    __tablename__ = 'science'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)