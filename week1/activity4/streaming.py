
import asyncio
from fastapi import APIRouter
from fastapi.responses import StreamingResponse

router = APIRouter()


# Async endpoint
@router.get("/async-info")
async def async_info():
    await asyncio.sleep(2)

    return {
        "message": "Async operation completed",
        "status": "success"
    }


# Generate Server-Sent Events
async def generate_events():
    messages = [
        "Welcome to MAF Agent Builder",
        "Starting agent workflow",
        "Processing request",
        "Generating response",
        "Workflow completed"
    ]

    for message in messages:
        yield f"data: {message}\n\n"
        await asyncio.sleep(1)


# SSE streaming endpoint
@router.get("/stream")
async def stream_data():
    return StreamingResponse(
        generate_events(),
        media_type="text/event-stream"
    )
