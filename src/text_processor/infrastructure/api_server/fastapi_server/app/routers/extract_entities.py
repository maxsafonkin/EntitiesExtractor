import typing

from fastapi import APIRouter, status

from text_processor import usecases
from . import views


router = APIRouter()
extractor_use_cases: usecases.ExtractorUseCases | None = None


@router.post(
    "/extract",
    response_model=typing.Union[
        views.responses.ServiceErrorResponse, views.responses.EntitiesResponse
    ],
)
def extract_entities(
    text: str,
) -> views.responses.EntitiesResponse | views.responses.ServiceErrorResponse:
    error_code: int | None = None
    error_message: str | None = None

    try:
        entities = extractor_use_cases.extract(text)
    except usecases.errors.UnsupportedLanguage as exc:
        error_code = status.HTTP_400_BAD_REQUEST
        error_message = str(exc)
    except usecases.errors.ExtractionError as exc:
        error_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        error_message = str(exc)

    if error_code is not None and error_message is not None:
        return views.responses.ServiceErrorResponse.new(
            code=error_code, message=error_message
        )

    return views.responses.EntitiesResponse.new(
        entities=[entity.to_dict() for entity in entities]
    )
