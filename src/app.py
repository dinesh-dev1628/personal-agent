from fastapi import FastAPI
import uvicorn
import traceback

from src.utils.env_data import settings
import src.ai.brain as brain

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the personal agent"}


@app.post("/habit-maker")
async def habit_generator(prompt: str):
    try:

        result = await brain.habit_maker(prompt)

        return result

    except Exception as e:
        print("🔥 HABIT MAKER ERROR:")
        print(str(e))
        traceback.print_exc()

        return {
            "error": str(e)
        }


@app.post("/coding-assistant")
async def coding_trainer(prompt: str):
    try:

        result = await brain.coding_assistant(prompt)

        return result

    except Exception as e:
        print("🔥 CODING ASSISTANT ERROR:")
        print(str(e))
        traceback.print_exc()

        return {
            "error": str(e)
        }


@app.post("/general-assistant")
async def general_chat(prompt: str):
    try:
        result = await brain.general_assistant(prompt)

        return result

    except Exception as e:
        print("🔥 GENERAL ASSISTANT ERROR:")
        print(str(e))
        traceback.print_exc()

        return {
            "error": str(e)
        }


if __name__ == "__main__":
    uvicorn.run(
        "src.app:app",
        host=settings.host,
        port=settings.port
    )