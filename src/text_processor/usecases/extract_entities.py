from text_processor import entities
from . import interfaces, errors


class ExtractorUseCases:
    def __init__(self, extractor: interfaces.Extractor) -> None:
        self._extractor = extractor

    def extract(self, text: str) -> list[entities.NamedEntity]:
        try:
            return self._extractor.extract_entities(text)
        except interfaces.errors.UnsupportedLanguage as exc:
            raise errors.UnsupportedLanguage(str(exc)) from exc
        except interfaces.errors.ExtractorError as exc:
            raise errors.ExtractionError(str(exc)) from exc
