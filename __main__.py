"""Entrypoint for the application."""

import uvicorn

from src.config.settings import settings


def run() -> None:
    """Run the application."""
    uvicorn.run(
        "src.api.app:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
    )


if __name__ == "__main__":
    run()
