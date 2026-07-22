from fastapi import FastAPI
from app.core.config import settings
from app.api.endpoints.v1.health import router as health_router
from app.api.endpoints.v1.search import router as search_router
from app.api.endpoints.v1.ollama import router as ollama_router

def create_app() -> FastAPI:
    """Create a FastAPI application instance."""
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description="An agentic RAG system for the ArXiv dataset.",
    )
    app.include_router(health_router, prefix=settings.API_PREFIX, tags=["health"])
    app.include_router(search_router, prefix=settings.API_PREFIX, tags=["search"])
    app.include_router(ollama_router, prefix=settings.API_PREFIX, tags=["ollama"])
    @app.get("/")
    async def root():
        return {
            "service": "rag-core",
            "version": settings.VERSION,
            "status": "healthy",
        }
    return app
app = create_app()