from typing import Self

from pydantic import BaseModel, Field, StrictInt, StrictStr


class DataResponse(BaseModel):
    result: dict = Field(default_factory=dict)


class Entity(BaseModel):
    tag: StrictStr = Field(description="Entity tag.")
    text: StrictStr = Field(description="Entity text.")


class EntitiesResponse(BaseModel):
    result: list[Entity]

    @classmethod
    def new(cls, entities: list[dict[str, str]]) -> Self:
        return cls(result=[Entity(**entity) for entity in entities])


class ServiceError(BaseModel):
    code: StrictInt = Field(description="Error code.")
    message: StrictStr = Field(description="Description of the error.")


class ServiceErrorResponse(BaseModel):
    error: ServiceError

    @classmethod
    def new(cls, code: int, message: str) -> Self:
        return cls(error=ServiceError(code=code, message=message))


class HTTPErrorResponse(BaseModel):
    message: str = Field(example="Description of the error.")
