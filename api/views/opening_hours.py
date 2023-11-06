from typing import List
from api.models import OpeningHoursInput
from api.models import OpeningHour
from api.utils import convert_unix_to_string


def views_opening_hours(opening_hours: OpeningHoursInput):
    response = {
        "Monday": format_hours(opening_hours.monday + opening_hours.tuesday[:1]),
        "Tuesday": format_hours(opening_hours.tuesday + opening_hours.wednesday[:1]),
        "Wednesday": format_hours(opening_hours.wednesday + opening_hours.thursday[:1]),
        "Thursday": format_hours(opening_hours.thursday + opening_hours.friday[:1]),
        "Friday": format_hours(opening_hours.friday + opening_hours.saturday[:1]),
        "Saturday": format_hours(opening_hours.saturday + opening_hours.sunday[:1]),
        "Sunday": format_hours(opening_hours.sunday + opening_hours.monday[:1]),
    }
    return response


def format_hours(opening_hours: List[OpeningHour]) -> str:
    formatted_hours = []
    current_open = None

    for entry in opening_hours:
        if entry.type == "open":
            current_open = entry
        else:
            if current_open:
                formatted_hours.append(
                    f"{convert_unix_to_string(current_open.value)} - {convert_unix_to_string(entry.value)}"
                )
                current_open = None

    if len(formatted_hours) == 0:
        return "Closed"
    return ", ".join(formatted_hours)
