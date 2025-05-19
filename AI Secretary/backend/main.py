from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import CalendarEvent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/test")
async def test():
    return {"message": "Hello from FastAPI!"}

@app.get("/test-event", response_model=CalendarEvent)
async def test_event():
    return CalendarEvent(
        id="123e4567-e89b-12d3-a456-426614174000",
        user_id="user_1",
        title="Sample Event",
        description="This is a test event.",
        start_time="2024-05-20T10:00:00Z",
        end_time="2024-05-20T11:00:00Z",
        location="Online",
        created_at="2024-05-19T12:00:00Z",
        updated_at="2024-05-19T12:00:00Z",
        external_id=None,
        recurrence=None,
        source="manual"
    ) 