from api.views import format_hours
from api.views import views_opening_hours
from api.models import OpeningHoursInput, OpeningHour


def test_format_hours():
    opening_hours = [
        OpeningHour(type="open", value=3600),
        OpeningHour(type="close", value=7200),
        OpeningHour(type="open", value=14400),
        OpeningHour(type="close", value=21600),
    ]
    formatted = format_hours(opening_hours)
    expected = "1 AM - 2 AM, 4 AM - 6 AM"
    assert formatted == expected


def test_format_hours_closed():
    opening_hours = []
    formatted = format_hours(opening_hours)
    expected = "Closed"
    assert formatted == expected


def test_views_opening_hours():
    opening_hours_input = OpeningHoursInput(
        monday=[
            OpeningHour(type="open", value=3600),
            OpeningHour(type="close", value=7200)
        ],
        tuesday=[
            OpeningHour(type="open", value=14400),
            OpeningHour(type="close", value=21600)
        ],
        wednesday=[],
        thursday=[],
        friday=[],
        saturday=[],
        sunday=[
            OpeningHour(type="open", value=43200),
            OpeningHour(type="close", value=75600)
        ]
    )

    formatted_hours = views_opening_hours(opening_hours_input)

    expected = {
        "Monday": "1 AM - 2 AM",
        "Tuesday": "4 AM - 6 AM",
        "Wednesday": "Closed",
        "Thursday": "Closed",
        "Friday": "Closed",
        "Saturday": "Closed",
        "Sunday": "12 PM - 9 PM",
    }

    assert formatted_hours == expected


def test_views_opening_hours_complicated_data():
    opening_hours_input = OpeningHoursInput(
        monday=[
            OpeningHour(type="close", value=1000),
            OpeningHour(type="open", value=28800),
            OpeningHour(type="close", value=36001),
            OpeningHour(type="open", value=39600),
            OpeningHour(type="close", value=45678),
        ],
        tuesday=[
            OpeningHour(type="open", value=14400),
            OpeningHour(type="close", value=21600),
        ],
        wednesday=[],
        thursday=[
            OpeningHour(type="open", value=37800),
            OpeningHour(type="close", value=64800),
        ],
        friday=[
            OpeningHour(type="open", value=36000),
        ],
        saturday=[
            OpeningHour(type="close", value=3600),
            OpeningHour(type="open", value=36000),
        ],
        sunday=[
            OpeningHour(type="close", value=3605),
            OpeningHour(type="open", value=43200),
            OpeningHour(type="close", value=75600),
            OpeningHour(type="open", value=86399),
        ]
    )

    formatted_hours = views_opening_hours(opening_hours_input)

    expected = {
        "Monday": "8 AM - 10:00:01 AM, 11 AM - 12:41:18 PM",
        "Tuesday": "4 AM - 6 AM",
        "Wednesday": "Closed",
        "Thursday": "10:30 AM - 6 PM",
        "Friday": "10 AM - 1 AM",
        "Saturday": "10 AM - 1:00:05 AM",
        "Sunday": "12 PM - 9 PM, 11:59:59 PM - 12:16:40 AM",
    }

    assert formatted_hours == expected
