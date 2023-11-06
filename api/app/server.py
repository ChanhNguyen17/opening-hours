from fastapi import FastAPI
from api.routers import opening_hours_router


def add_routers(app: FastAPI) -> None:
    app.include_router(
        opening_hours_router,
        prefix="/restaurant-opening-hours",
        tags=["restaurant-opening-hours"]
    )
