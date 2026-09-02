from pydantic_ai import Agent
from dotenv import load_dotenv
load_dotenv()

import models.basemodel as basemodel
from utils.settings import model_name

def habit_maker(data):

    habit_agent = Agent(
        model_name,
        output_type=basemodel.HabitEntry,
        instructions='You are a helpful assistant that helps users create a list of habits based on their input. Please provide a list of habits in the output by their providing timeperiod or infromation like the habit cycle.',
    )

    result = habit_agent.run_sync(data)
    print(result.output.tips)


def coding_assistant(data):

    coding_agent = Agent(
        model_name,
        output_type=basemodel.CodingEntry,
        instructions='You are a helpful assistant that helps users create coding skills and guidance based on their input. Please provide a valuable coding tips',
    )

    result = coding_agent.run_sync(data)
    print(result.output.tips)


