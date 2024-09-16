import uvicorn

from text_processor import usecases
from .app import get_app
from ..api_server import APIServer


class FastAPIServer(APIServer):
    __SERVER_PORT = 7890

    def __init__(self, extractor_use_cases: usecases.ExtractorUseCases) -> None:
        super().__init__(extractor_use_cases)

    def start(self) -> None:
        config = uvicorn.Config(
            app=get_app(self._extractor_use_cases),
            host="0.0.0.0",
            port=self.__SERVER_PORT,
        )
        server = uvicorn.Server(config)
        server.run()
