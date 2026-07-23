from app.services.ollama.ollama_client import OllamaClient
from app.services.prompt_builder import prompt_builder

ollama_client = OllamaClient()


class LLMService:
    """
    Handles answer generation using the local LLM.
    """

    async def generate(self, question: str, context: list[dict]) -> str:
        # Step 1: Build the prompt
        prompt = prompt_builder.build(question, context)

        # Step 2: Generate the answer with Ollama
        answer = await ollama_client.generate(prompt)

        return answer


llm_service = LLMService()