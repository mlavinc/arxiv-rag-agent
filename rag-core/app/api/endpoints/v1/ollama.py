from fastapi import APIRouter

from app.services.ollama.ollama_client import OllamaClient

router = APIRouter()

client = OllamaClient()


@router.get("/ollama/health")
async def ollama_health():
    healthy = await client.health_check()

    return {
        "service": "ollama",
        "healthy": healthy,
    }


@router.get("/ollama/models")
async def list_models():
    return await client.list_models()