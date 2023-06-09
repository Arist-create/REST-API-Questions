from src.database.model import Question
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

async def check_duplicate(db: AsyncSession, question_text: str) -> bool:
    response: Question | None = await db.execute(select(Question).filter(Question.question_text == question_text))
    try:
        response.scalars().one()
        return True
    except:
        return False