from fastapi import FastAPI
from src.app.routers import add_routers
from src.app.exception_handlers import add_exception_handlers

app = FastAPI()

add_routers(app)
add_exception_handlers(app)
