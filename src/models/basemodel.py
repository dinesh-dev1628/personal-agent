from pydantic import BaseModel, Field


class HabitEntry(BaseModel):
    activity: str
    duration: int
    tips: str = Field(description="A short actionable tip")


class HabitResponse(BaseModel):
    habits: list[HabitEntry] = Field(
        default_factory=list,
        description="Extracted, trackable habit plans. Leave empty if the input "
                    "doesn't describe a clear habit or goal — use `clarification` instead.",
    )
    clarification: str | None = Field(
        default=None,
        description="A short, specific question to ask the user when their input "
                    "is too vague, unrelated, or incomplete to extract a real habit "
                    "plan from (e.g. a greeting, or a goal with no actionable detail "
                    "at all). Set to null whenever `habits` was successfully populated.",
    )


class CodingResponse(BaseModel):
    response: str = Field(
        description="A complete helpful coding answer formatted using Markdown. "
                    "Use headings, bullet points, inline code, and fenced code blocks where appropriate."
    )


class GeneralResponse(BaseModel):
    response: str = Field(
        description="A complete, conversational answer to the user's message, "
                    "formatted using Markdown where it aids readability (lists, "
                    "emphasis, code spans) but without forcing structure onto a "
                    "simple reply."
    )