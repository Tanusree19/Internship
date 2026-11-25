
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Literal

router = APIRouter()


# Request model with validation
class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=5, max_length=500)
    status: Literal["pending", "in_progress", "completed"] = "pending"


# Response model
class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    status: str


tasks = {}
next_id = 1


# GET all tasks
@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    return list(tasks.values())


# GET task by ID
@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]


# POST create task
@router.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate):
    global next_id

    task_data = task.model_dump()
    task_data["id"] = next_id

    tasks[next_id] = task_data
    next_id += 1

    return task_data


# PUT update task
@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskCreate):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    task_data = task.model_dump()
    task_data["id"] = task_id

    tasks[task_id] = task_data
    return task_data


# DELETE task
@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    del tasks[task_id]
    return {"message": "Task deleted successfully"}
