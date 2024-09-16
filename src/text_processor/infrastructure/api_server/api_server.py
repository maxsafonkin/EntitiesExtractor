import abc

from text_processor import usecases


class APIServer(abc.ABC):
    def __init__(self, extractor_use_cases: usecases.ExtractorUseCases) -> None:
        self._extractor_use_cases = extractor_use_cases

    @abc.abstractmethod
    def start(self) -> None:
        pass
