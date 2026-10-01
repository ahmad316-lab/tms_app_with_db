from fastapi import FastAPI
from app.routers.task_router import router
from app.models.model import TaskSchema
from app.schemas.schema import Task
from app.utils.db import get_session
from app.errors.errors import task_not_found, TaskNotFound

app = FastAPI()
app.include_router(router)
app.add_exception_handler(
    TaskNotFound,
    task_not_found
)