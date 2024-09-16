import abc

from text_processor import entities


class Extractor(abc.ABC):
    @abc.abstractmethod
    def extract_entities(self, text: str) -> list[entities.NamedEntity]:
        pass
