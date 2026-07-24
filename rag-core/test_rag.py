import asyncio

from app.services.rag.rag_service import rag_service


QUESTION = "What is PyramidTNT?"


async def main():
    print(f"Question: {QUESTION}\n")

    response = await rag_service.search(QUESTION)

    print("Answer:")
    print(response.answer)
    print()

    print("Sources:")
    for source in response.sources:
        print(
            f"- {source.title} "
            f"(document_id={source.document_id}, "
            f"chunk={source.chunk_index}, "
            f"score={source.score:.4f})"
        )

    assert response.answer, "Expected a non-empty answer from the LLM"

    print("\nRAG end-to-end validation PASSED")


asyncio.run(main())
