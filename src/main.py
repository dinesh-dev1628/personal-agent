
from fastapi import FastAPI
import uvicorn

from utils.env_data import settings

app = FastAPI()


@app.get("/")
async def root():
    return {"Welcome to the personal agent"}

@app.post("/habit-maker")
async def habit_generator(prompt: str):
    from ai.brain import habit_maker
    result = await habit_maker(prompt)
    return {"message": "Habit maker executed successfully.", "result": result}


@app.post("/coding-assistant")
async def coding_trainer(prompt: str):
    from ai.brain import coding_assistant
    result = await coding_assistant(prompt)
    return {"message": "Coding assistant executed successfully.", "result": result}

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.host, port=settings.port, reload=True)