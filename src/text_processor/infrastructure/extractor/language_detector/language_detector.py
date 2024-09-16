from pathlib import Path

import fasttext

from . import errors


class LanguageDetector:
    def __init__(self) -> None:
        model_path = Path.cwd() / "src" / "text_processor" / "infrastructure" / "extractor" / "language_detector" /"model" / "model.bin"
        self._model = fasttext.load_model(str(model_path))

    def detect_language(self, text: str) -> str:
        try:
            language, _ = self._model.predict(text)
        except Exception as exc:
            raise errors.LanguageDetectorError(str(exc)) from exc

        language = language[0].replace("__label__", "")
        return language
