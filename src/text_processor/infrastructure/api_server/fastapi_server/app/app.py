from fastapi import FastAPI

from text_processor import usecases
from . import routers
from .error_handlers import DEFAULT_ERROR_RESPONSES, EXCEPTION_HANDLERS


def get_app(extractor_use_cases: usecases.ExtractorUseCases) -> FastAPI:
    app = FastAPI(
        exception_handlers=EXCEPTION_HANDLERS, responses=DEFAULT_ERROR_RESPONSES
    )

    routers.extract_entities.extractor_use_cases = extractor_use_cases

    app.include_router(routers.extract_entities.router, prefix="/api/v1")

    return app
