from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_render_opening_hours():
    valid_input = {
        "monday": [],
        "tuesday": [
            {"type": "open", "value": 3600},
            {"type": "close", "value": 7200}
        ],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": []
    }

    response = client.post("/restaurant-opening-hours", json=valid_input)

    assert response.status_code == 200
    assert response.json() == {
        "Monday": "Closed",
        "Tuesday": "1 AM - 2 AM",
        "Wednesday": "Closed",
        "Thursday": "Closed",
        "Friday": "Closed",
        "Saturday": "Closed",
        "Sunday": "Closed",
    }


def test_render_opening_hours_invalid_format():
    invalid_input = {
        "monday": "invalid_data",  # Invalid format
        "tuesday": [
            {"type": "open", "value": 3600},
            {"type": "close", "value": 7200}
        ],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": []
    }

    response = client.post("/restaurant-opening-hours", json=invalid_input)

    assert response.status_code == 400


def test_render_opening_hours_empty_input():
    empty_input = {
        "monday": [],
        "tuesday": [],
        "wednesday": [],
        "thursday": [],
        "friday": [],
        "saturday": [],
        "sunday": []
    }

    response = client.post("/restaurant-opening-hours", json=empty_input)

    assert response.status_code == 200
    assert response.json() == {
        "Monday": "Closed",
        "Tuesday": "Closed",
        "Wednesday": "Closed",
        "Thursday": "Closed",
        "Friday": "Closed",
        "Saturday": "Closed",
        "Sunday": "Closed",
    }
