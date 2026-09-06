from fastapi import FastAPI
import uvicorn

from src.utils.env_data import settings

app = FastAPI()


@app.get("/")
async def root():
    return {"Welcome to the personal agent"}


@app.post("/habit-maker")
async def habit_generator(prompt: str):
    from ai.brain import habit_maker
    result = await habit_maker(prompt)
    return result


@app.post("/coding-assistant")
async def coding_trainer(prompt: str):
    from ai.brain import coding_assistant
    result = await coding_assistant(prompt)
    return result


@app.post("/general-assistant")
async def general_chat(prompt: str):
    from ai.brain import general_assistant
    result = await general_assistant(prompt)
    return result


if __name__ == "__main__":
    uvicorn.run("src.app:app", "--host 0.0.0.0", "--port", "$PORT")