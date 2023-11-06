import pytest
from api.models import OpeningHour, OpeningHoursInput
from pydantic import ValidationError


def test_opening_hour_model():
    # Valid opening hour
    opening_hour = OpeningHour(type="open", value=3600)
    assert opening_hour.type == "open"
    assert opening_hour.value == 3600

    # Invalid opening hour (missing 'type')
    with pytest.raises(ValidationError):
        opening_hour = OpeningHour(value=3600)


def test_opening_hours_input_model():
    # Valid opening hours input
    opening_hours_input = OpeningHoursInput(
        monday=[{"type": "open", "value": 3600}, {"type": "close", "value": 7200}],
        tuesday=[],
        wednesday=[],
        thursday=[],
        friday=[{"type": "open", "value": 36000}],
        saturday=[{"type": "close", "value": 3600}],
        sunday=[]
    )
    assert len(opening_hours_input.monday) == 2
    assert len(opening_hours_input.tuesday) == 0
    assert len(opening_hours_input.friday) == 1
    assert len(opening_hours_input.saturday) == 1

    # Invalid opening hours input (missing 'monday' key)
    with pytest.raises(ValidationError):
        opening_hours_input = OpeningHoursInput(
            tuesday=[],
            wednesday=[],
            thursday=[],
            friday=[],
            saturday=[{"type": "open", "value": 3600}, {"type": "close", "value": 7200}],
            sunday=[]
        )

    # Invalid opening hours input (invalid opening hour)
    with pytest.raises(ValidationError):
        opening_hours_input = OpeningHoursInput(
            monday=[],
            tuesday=[],
            wednesday=[{"type": "open", "value": "invalid_time"}, {"type": "close", "value": 7200}],
            thursday=[],
            friday=[],
            saturday=[],
            sunday=[]
        )
