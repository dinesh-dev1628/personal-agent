from pydantic import BaseModel

class HabitEntry(BaseModel):
   activity: str
   duration: int
   tips: str

class CodingEntry(BaseModel):
   skill: str
   level: str
   tips: str