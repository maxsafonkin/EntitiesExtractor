from fastapi import Request, status
from fastapi.responses import JSONResponse

from text_processor.usecases import errors as usecases_err
from .routers.views.responses import HTTPErrorResponse, ServiceErrorResponse


async def _app_exception_handler(
    request: Request, exc: usecases_err.ExtractionError
) -> JSONResponse:
    response = ServiceErrorResponse.new(code=status.HTTP_200_OK, message=str(exc))
    return JSONResponse(status_code=status.HTTP_200_OK, content=response.dict())


async def _unhandled_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    err_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    response = ServiceErrorResponse.new(
        code=err_code, message="Unhandled error occurred."
    )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response.dict(),
    )


_DEFAULT_ERROR_CODES = [
    status.HTTP_405_METHOD_NOT_ALLOWED,
    status.HTTP_422_UNPROCESSABLE_ENTITY,
]

DEFAULT_ERROR_RESPONSES = {
    error_code: {"model": HTTPErrorResponse} for error_code in _DEFAULT_ERROR_CODES
}

EXCEPTION_HANDLERS = {
    usecases_err.ExtractionError: _app_exception_handler,
    Exception: _unhandled_exception_handler,
}
