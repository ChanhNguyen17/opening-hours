from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


def add_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(RequestValidationError)
    async def request_validation_exception_handler(_, exc):
        detail = exc.errors()
        return JSONResponse(
            status_code=400,
            content={"detail": detail}
        )
