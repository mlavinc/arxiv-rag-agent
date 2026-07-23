class PromptBuilder:
    """
    Builds prompts for the LLM using retrieved context.
    """

    def build(self, question: str, context: list[dict]) -> str:
        context_text = "\n\n".join(
            f"Chunk {i + 1}:\n{chunk['document']}"
            for i, chunk in enumerate(context)
        )

        return f"""You are an AI assistant specialized in scientific literature.

Answer the user's question using ONLY the provided context.

If the answer cannot be found in the provided context, explicitly say that you don't have enough information.

Context:

{context_text}

Question:
{question}

Answer:
"""


prompt_builder = PromptBuilder()