from pydantic import BaseModel

class Task(BaseModel):
    task_name: str
    priority: str
    status: str