from pydantic import BaseModel


class GetQuestionsResponseModel(BaseModel):
    last_question: str