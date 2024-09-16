class ExtractorError(Exception):
    """Base extractor exception"""

    pass


class UnableToProcessText(ExtractorError):
    """Raised whenever extractor can't process text"""

    pass


class UnsupportedLanguage(ExtractorError):
    """Raised whenever extractor faces unsupported language"""

    pass


class InternalError(ExtractorError):
    """Raised whenever extractor can't process text due to internal error"""

    pass
