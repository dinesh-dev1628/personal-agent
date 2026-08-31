from pydantic import BaseModel

class HabitEntry(BaseModel):
   listofhabits: list[str]