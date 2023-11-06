from fastapi import APIRouter
from typing import Dict

from api.models import OpeningHoursInput
from api.views import views_opening_hours

opening_hours_router = APIRouter()


@opening_hours_router.post("/", response_model=Dict[str, str])
async def render_opening_hours(opening_hours: OpeningHoursInput):
    response = views_opening_hours(opening_hours)
    return response
