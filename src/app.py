from pydantic_ai import Agent
from dotenv import load_dotenv
load_dotenv()

from models.basemodel import HabitEntry
from utils.settings import model_name

def habit_maker(data):

    habit_agent = Agent(
        model_name,
        output_type=HabitEntry,
        instructions='You are a helpful assistant that helps users create a list of habits based on their input. Please provide a list of habits in the output by their providing timeperiod .',
    )

    result = habit_agent.run_sync(data)
    print(result.output.listofhabits)

if __name__ == "__main__":

    user_input = input("Please enter your minutes for providing a useful lst of habits: ")
    habit_maker(user_input)