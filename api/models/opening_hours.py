from typing import List
from pydantic import BaseModel


class OpeningHour(BaseModel):
    type: str
    value: int


class OpeningHoursInput(BaseModel):
    monday: List[OpeningHour]
    tuesday: List[OpeningHour]
    wednesday: List[OpeningHour]
    thursday: List[OpeningHour]
    friday: List[OpeningHour]
    saturday: List[OpeningHour]
    sunday: List[OpeningHour]
