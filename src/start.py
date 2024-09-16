import os

from text_processor import infrastructure, usecases
from utils import env


def main() -> int:
    try:
        extractor = infrastructure.Extractor(env.USE_GPU)
        extractor_use_cases = usecases.ExtractorUseCases(extractor)
        api_server = infrastructure.FastAPIServer(extractor_use_cases)

        api_server.start()
    except Exception as exc:
        print(exc)
        return 1

    return 0


if __name__ == "__main__":
    exit_code = main()
    os._exit(exit_code)
