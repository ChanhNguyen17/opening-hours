from fastapi import FastAPI
from src.app import add_routers
from src.app import add_exception_handlers

app = FastAPI()

add_routers(app)
add_exception_handlers(app)
