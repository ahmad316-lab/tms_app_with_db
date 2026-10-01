from fastapi import APIRouter, status, Depends
from app.schemas.schema import Task
from app.utils.db import get_session
from sqlalchemy.orm import Session
from app.controllers import controllers


router = APIRouter(prefix="/api/v1")


# CRUD Endpoints
@router.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: Task, db : Session = Depends(get_session)):
    return controllers.create_task(task, db)

@router.get("/tasks", status_code=status.HTTP_200_OK)
def get_tasks(s: str, p: str, t: str , db : Session = Depends(get_session)):
    return controllers.get_tasks(s,p,t, db)

@router.get("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def get_task_by_id(task_id: int, db : Session = Depends(get_session)):
    return controllers.get_task_by_id(task_id, db)

@router.put("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def update_task(task_id: int, task: Task, db : Session = Depends(get_session)):
    return controllers.update_task(task_id, task, db)

@router.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def delete_task(task_id: int, db : Session = Depends(get_session)):
    return controllers.delete_task(task_id, db)





