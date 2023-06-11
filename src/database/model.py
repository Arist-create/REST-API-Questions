from src.database.main import Base
from sqlalchemy import Column, Integer, String


class Question(Base):
    __tablename__ = "Questions"

    id = Column(Integer, primary_key=True)
    question_text = Column(String)
    answer_text = Column(String)
    date = Column(String)
