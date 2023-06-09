from src.database.model import Question
from sqlalchemy.ext.asyncio import AsyncSession


async def put_questions_db(db: AsyncSession, request: dict) -> None:
    question: Question = Question(question_text=request['question'],
                        answer_text=request['answer'],
                        date=request['created_at'])
    db.add(question)
    await db.commit()
