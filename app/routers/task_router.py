from fastapi import APIRouter, status



router = APIRouter(prefix="/api/v1")


# CRUD Endpoints
@router.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task():
    pass

@router.get("/tasks", status_code=status.HTTP_200_OK)
def get_tasks():
    pass

@router.get("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def get_task_by_id():
    pass

@router.put("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def update_task():
    pass
@router.delete("/tasks/{task_id}", status_code=status.HTTP_200_OK)
def delete_task():
    pass





