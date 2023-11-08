from fastapi import APIRouter
from typing import Dict

from src.models import OpeningHoursInput
from src.views import views_opening_hours

opening_hours_router = APIRouter()


@opening_hours_router.post("/", response_model=Dict[str, str])
async def render_opening_hours(opening_hours: OpeningHoursInput):
    response = views_opening_hours(opening_hours)
    return response
