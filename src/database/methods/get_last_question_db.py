from src.database.model import Question
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_last_question_db(db: AsyncSession) -> str | None:
    response = await db.execute(select(Question).order_by(Question.id.desc()))
    result = response.scalars().first()
    if result is None:
        return None
    else:
        return result.question_text
