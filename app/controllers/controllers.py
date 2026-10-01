from app.models.model import TaskSchema
from app.schemas.schema import Task
from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete
from app.errors.errors import TaskNotFound


def create_task(task: Task, db: Session):
    new_task = TaskSchema(
        task_name = task.task_name,
        priority = task.priority,
        status = task.status
    )

    db.add(new_task)
    db.commit()

    return {
        "message" : "Task Created"
    }

def get_tasks(
        status: str | None = None,
        priority: str | None = None,
        search: str | None = None,
        db: Session = None
):
  stmt = select(TaskSchema)
  if status is not None:
      stmt = stmt.where(TaskSchema.status == status)

  if priority is not None:
      stmt = stmt.where(TaskSchema.priority == priority)

  if search is not None:
      stmt = stmt.where(TaskSchema.task_name.ilike(f"%{search}%"))

  res = db.execute(stmt)

  return res.scalars().all()



def get_task_by_id(t_id: int, db: Session):
    t = select(TaskSchema).where(TaskSchema.id == t_id)

    res = db.execute(t)

    task = res.scalars().first()

    if task is None:
        raise TaskNotFound

    return task


def update_task(t_id: int, task: Task, db: Session):

    stmt = (
    update(TaskSchema)
    .where(TaskSchema.id == t_id)
    .values(
        task_name=task.task_name,
        priority=task.priority,
        status=task.status
    )
)

    res = db.execute(stmt)

    if res.rowcount == 0:
        raise TaskNotFound

    db.commit()

    return {
        "message" : "Task Updated"
    }

def delete_task(t_id: int, db: Session):

    stmt = delete(TaskSchema).where(TaskSchema.id == t_id)

    res = db.execute(stmt)

    if res.rowcount == 0:
        raise TaskNotFound

    db.commit()

    return {
        "message" : "Task Deleted"
    }


