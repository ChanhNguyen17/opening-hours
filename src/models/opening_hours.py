from typing import List, Dict
from pydantic import BaseModel


class OpeningHour(BaseModel):
    type: str
    value: int

    def to_dict(self) -> Dict[str, str]:
        return {
            "type": self.type,
            "value": self.value
        }


class OpeningHoursInput(BaseModel):
    monday: List[OpeningHour]
    tuesday: List[OpeningHour]
    wednesday: List[OpeningHour]
    thursday: List[OpeningHour]
    friday: List[OpeningHour]
    saturday: List[OpeningHour]
    sunday: List[OpeningHour]
