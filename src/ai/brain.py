from pydantic_ai import Agent
from pydantic_ai.output import NativeOutput
from dotenv import load_dotenv
load_dotenv()

import models.basemodel as basemodel
from utils.settings import model_name
from data.instructions import coding_instructions, habit_instructions, general_instructions

# groq:openai/gpt-oss-120b is unreliable with pydantic-ai's default tool-based
# structured output (it emits its own tool names, e.g. 'json', instead of
# calling the internal 'final_result' tool pydantic-ai expects, and then
# burns through all retries failing the same way). Wrapping output_type in
# NativeOutput tells pydantic-ai to request structured output via Groq's
# native response_format / JSON-schema mode instead of tool-calling, which
# Groq's own docs use for this exact model.

habit_agent = Agent(
    model_name,
    output_type=NativeOutput(basemodel.HabitResponse),
    instructions=habit_instructions,
    retries=3,
)

coding_agent = Agent(
    model_name,
    output_type=NativeOutput(basemodel.CodingResponse),
    instructions=coding_instructions,
    retries=3,
)

general_agent = Agent(
    model_name,
    output_type=NativeOutput(basemodel.GeneralResponse),
    instructions=general_instructions,
    retries=3,
)


async def habit_maker(data):
    result = await habit_agent.run(data)
    return result.output


async def coding_assistant(data):
    result = await coding_agent.run(data)
    return result.output


async def general_assistant(data):
    result = await general_agent.run(data)
    return result.output