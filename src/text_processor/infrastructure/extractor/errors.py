from text_processor import usecases


class ExtractorError(usecases.interfaces.errors.ExtractorError):
    pass


class UnsupportedLanguage(usecases.interfaces.errors.UnsupportedLanguage):
    pass


class GPUIsUnavailable(usecases.interfaces.errors.InternalError):
    pass


class CUDAOutOfMemory(usecases.interfaces.errors.InternalError):
    pass
