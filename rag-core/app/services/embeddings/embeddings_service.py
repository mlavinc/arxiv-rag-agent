from app.services.ollama.ollama_client import OllamaClient


class EmbeddingsService:
    """
    Handles embedding generation using Ollama.
    """

    def __init__(self):
        self.ollama_client = OllamaClient()

    async def embed(self, text: str) -> list[float]:
        return await self.ollama_client.generate_embedding(text)


embeddings_service = EmbeddingsService()