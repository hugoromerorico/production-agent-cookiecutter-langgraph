# Third-party imports
from fastapi import FastAPI
from loguru import logger
import sys
import os

# Route imports
from app.routes import system
from app.config.config import settings
from app.infrastructure.llm_service import LLMService
import uvicorn



def setup_dependencies(app: FastAPI) -> FastAPI:
    # Configure logging
    logger.remove()
    logger.add(sys.stderr, level=settings.log_level)

    """Setup dependencies for the application."""
    # Infrastructure layer
    app.state.llm_service = LLMService()
    app.include_router(system.router)

    # Application layer
    return app

app = FastAPI(title="rendered-project", version="0.1.0")
setup_dependencies(app)

if __name__ == "__main__":
    uvicorn.run(app, host=settings.server.host, port=settings.server.port)
