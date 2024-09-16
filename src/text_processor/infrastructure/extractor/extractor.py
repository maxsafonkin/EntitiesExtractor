from pathlib import Path

import flair
import torch
from flair.data import Sentence
from flair.models import SequenceTagger

from text_processor import usecases, entities
from . import errors
from .language_detector import LanguageDetector
from .language_detector import errors as ld_errors


class Extractor(usecases.interfaces.Extractor):
    _SUPPORTED_TAGS = (
        "PER",
        "LOC",
        "DATE",
        "EVE",
        "ORG",
        "DIS",
        "MEDIA",
    )

    _SUPPORTED_LANGUAGES = "en"

    def __init__(self, use_gpu: bool = False) -> None:
        self._extractor = self._init_extractor(use_gpu)
        self._language_detector = LanguageDetector()

    def _init_extractor(self, use_gpu: bool) -> SequenceTagger:
        if use_gpu:
            self._set_gpu()

        model_path = Path.cwd() / "src" / "text_processor" / "infrastructure" / "extractor" / "model" / "model.pt"
        return SequenceTagger.load(model_path)

    def extract_entities(self, text: str) -> list[entities.NamedEntity]:
        sentence = Sentence(text)

        try:
            self._extractor.predict(sentence)
        except torch.cuda.OutOfMemoryError as exc:
            raise errors.CUDAOutOfMemory(str(exc))
        except Exception as exc:
            raise errors.ExtractorError(str(exc)) from exc
        print(sentence.get_spans("ner"))
        return [
            entities.NamedEntity(tag=entities.Tag(span.tag), text=span.text)
            for span in sentence.get_spans("ner")
            if span.tag in self._SUPPORTED_TAGS
        ]

    def _check_language(self, text: str) -> None:
        try:
            language = self._language_detector.detect_language(text)
        except ld_errors.LanguageDetectorError as exc:
            raise errors.ExtractorError(str(exc)) from exc

        if language not in self._SUPPORTED_LANGUAGES:
            msg_exc = f"Language {language} is not supported"
            raise errors.UnsupportedLanguage(msg_exc)

    @staticmethod
    def _set_gpu() -> None:
        if not torch.cuda.is_available():
            raise errors.GPUIsUnavailable("GPU is unavailable")

        flair.device = torch.device("cuda")
