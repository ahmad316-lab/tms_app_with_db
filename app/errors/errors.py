from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

app = FastAPI()

class TaskNotFound(Exception):
    pass

app.exception_handler(TaskNotFound)
async def task_not_found(
        request: Request,
        exc: TaskNotFound
):
    return JSONResponse(
        status_code= status.HTTP_404_NOT_FOUND,
        content=f"Task Not Found 😊 {str(exc)}"
    )
    


