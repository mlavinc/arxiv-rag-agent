from fastapi import FastAPI
from app.core.config import settings

def create_app() -> FastAPI:
    """Create a FastAPI application instance."""
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description="An agentic RAG system for the ArXiv dataset.",
    )
    @app.get("/")
    async def root():
        return {
            "service": "rag-core",
            "version": settings.VERSION,
            "status": "healthy",
        }
    return app
app = create_app()