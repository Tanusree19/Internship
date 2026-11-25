  
from fastapi import FastAPI

app = FastAPI(
    title="MAF Agent Builder",
    description="Learning FastAPI for the MAF Agent Builder project",
    version="1.0.0"
)

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
        "activity": "Week 1 - Activity 1"
    }
