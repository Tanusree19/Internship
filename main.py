
from fastapi import FastAPI

# Import Activity 2 router
from week1.activity2.routes import router as task_router

from week1.activity4.streaming import router as streaming_router
# Create FastAPI application first
app = FastAPI(
    title="MAF Agent Builder",
    description="Integrated internship learning project",
    version="1.0.0"
)

# Register Activity 2 router
app.include_router(task_router)
app.include_router(streaming_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to MAF Agent Builder",
        "status": "Application is running"
    }


@app.get("/about")
def about():
    return {
        "project": "MAF Agent Builder",
        "framework": "FastAPI",
        "week": 1,
        "activity": 1
    }
