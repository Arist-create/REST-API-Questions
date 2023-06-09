from src.database.main import Base
from sqlalchemy import Column, Integer, String


class Question(Base):
    __tablename__ = "Questions"

    id: int = Column(Integer, primary_key=True)
    question_text: str = Column(String)
    answer_text: str = Column(String)
    date: str = Column(String)
