from fastapi.responses import JSONResponse
import requests
from src.database.methods.put_questions_db import put_questions_db
from src.database.methods.get_last_question_db import get_last_question_db
from src.schemas.get_questions_request_model import GetQuestionsRequestModel
from src.database.methods.check_duplicate import check_duplicate
from sqlalchemy.ext.asyncio import AsyncSession
from requests.models import Response




async def get_questions_ctrl(db: AsyncSession, request: GetQuestionsRequestModel) -> JSONResponse:
    last_question: None | str  = await get_last_question_db(db)
    count: int = request.questions_num
    while True:
        if count == 0:
            break
        response = requests.get(f'https://jservice.io/api/random?count=1')
        if await check_duplicate(db, response.json()[0]['question']):
            continue
        await put_questions_db(db, response.json()[0])
        count -= 1
    if last_question is None:
        return JSONResponse(status_code=201, content={})
    return JSONResponse(status_code=201, content={'last_question': last_question})
