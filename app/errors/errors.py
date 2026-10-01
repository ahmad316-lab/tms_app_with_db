from fastapi import Request, status
from fastapi.responses import JSONResponse

class TaskNotFound(Exception):
    pass


async def task_not_found(
        request: Request,
        exc: TaskNotFound
):
    return JSONResponse(
        status_code= status.HTTP_404_NOT_FOUND,
        content=f"Task Not Found 😊 {str(exc)}"
    )
    


