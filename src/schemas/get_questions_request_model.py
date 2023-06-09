from pydantic import BaseModel


class GetQuestionsRequestModel(BaseModel):
    questions_num: int