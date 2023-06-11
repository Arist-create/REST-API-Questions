from src.database.model import Question
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

async def check_duplicate(db: AsyncSession, question_text: str) -> bool:
    response = await db.execute(select(Question).filter(Question.question_text == question_text))
    result = response.scalars().first()
    if result is None:
        return False
    else:
        return True
    