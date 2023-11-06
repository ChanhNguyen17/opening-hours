from fastapi import FastAPI
from api.app.server import add_routers
from api.app.exception_handler import add_exception_handlers

app = FastAPI()

add_routers(app)
add_exception_handlers(app)
