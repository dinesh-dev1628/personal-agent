
from fastapi import FastAPI
import uvicorn

from utils.env_data import settings

app = FastAPI()


@app.get("/")
async def root():
    return {"Welcome to the personal agent"}

@app.post("/habit-maker")
async def habit_maker(data: str):
    from ai.brain import habit_maker
    habit_maker(data)
    return {"message": "Habit maker executed successfully."}



if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.host, port=settings.port, reload=True)