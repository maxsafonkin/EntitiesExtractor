from enum import StrEnum


class Tag(StrEnum):
    PERSON = "PER"
    LOCATION = "LOC"
    DATE = "DATE"
    EVENT = "EVE"
    ORGANIZATION = "ORG"
    DISEASE = "DIS"
    MEDIA = "MEDIA"
