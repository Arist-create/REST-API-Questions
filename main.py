from fastapi import FastAPI
from src.database.main import init_db
from src.routers import get_questions_router

app = FastAPI()


@app.on_event("startup")
async def on_startup() -> None:
    await init_db()


app.include_router(get_questions_router.router)
