import http
from fastapi import APIRouter, Body
from src.controllers.get_questions_ctrl import get_questions_ctrl
from src.schemas.get_questions_response_model import GetQuestionsResponseModel
from src.schemas.get_questions_request_model import GetQuestionsRequestModel
from fastapi import Depends
from src.database.main import get_db
from sqlalchemy.ext.asyncio import AsyncSession
router = APIRouter()


@router.post(
    "/api/get_questions",
    response_model=GetQuestionsResponseModel,
    summary="Получить вопросы",
    status_code=http.HTTPStatus.CREATED,
    tags=["Получение"]
)
async def get_questions_router(
    data: GetQuestionsRequestModel = Body(), db: AsyncSession = Depends(get_db)
) -> GetQuestionsResponseModel:
    return await get_questions_ctrl(db, data)
