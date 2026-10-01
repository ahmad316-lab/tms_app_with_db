from fastapi import FastAPI
from app.routers.task_router import router
from app.models.model import TaskSchema
from app.schemas.schema import Task
from app.utils.db import get_session

app = FastAPI()
app.include_router(router)