# Third-party imports
from fastapi import FastAPI
from loguru import logger
import sys

# Route imports
from app.routes import system, chat, wf1
from app.config.config import settings
from app.application.chat import Chat
from app.application.use_case import UseCase
import uvicorn



def setup_dependencies(app: FastAPI) -> FastAPI:
    # Configure logging
    logger.remove()
    logger.add(sys.stderr, level=settings.log_level)

    """Setup dependencies for the application."""
    # Infrastructure layer
    app.state.chat = Chat()
    app.state.use_case = UseCase()
    app.include_router(system.router)
    app.include_router(chat.router)
    app.include_router(wf1.router)

    # Application layer
    return app

app = FastAPI(title="{{cookiecutter.project_name}}", version="0.1.0")
setup_dependencies(app)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.server.host, port=settings.server.port)
