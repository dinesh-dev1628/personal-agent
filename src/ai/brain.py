from pydantic_ai import Agent
from dotenv import load_dotenv
load_dotenv()

import models.basemodel as basemodel
from utils.settings import model_name

async def habit_maker(data):

    habit_agent = Agent(
        model_name,
        output_type=basemodel.HabitEntry,
        instructions='You are a helpful assistant that helps users create a list of habits based on their input. Please provide a list of habits in the output by their providing timeperiod or infromation like the habit cycle.',
    )

    result = await habit_agent.run(data)
    return result.output


async def coding_assistant(data):

    coding_agent = Agent(
        model_name,
        output_type=basemodel.CodingEntry,
        instructions='You are a helpful assistant that helps users create coding skills and guidance based on their input. Please provide a valuable coding tips',
    )
    
    result = await coding_agent.run(data)
    return result.output


