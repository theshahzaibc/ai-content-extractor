from fastapi import APIRouter, Depends
from app.workers.celery_worker import extract_task
from app.schemas.task import TaskCreate
from celery.result import AsyncResult

router = APIRouter()

tasks_store = {}


@router.post("/extract")
def submit_task(task: TaskCreate):
    celery_task = extract_task.delay(task.url)
    tasks_store[celery_task.id] = celery_task
    return {"task_id": celery_task.id, "status": "PENDING"}


@router.get("/task/{task_id}")
def get_task(task_id: str):
    celery_task: AsyncResult = tasks_store.get(task_id)
    if not celery_task:
        return {"error": "Task not found"}
    return {"task_id": task_id, "status": celery_task.status, "result": celery_task.result}
