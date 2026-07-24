import asyncio

from app.services.ingestion.ingestion_service import ingestion_service
from app.services.vector_db.vector_db_service import vector_db_service


async def main():
    # Reset collection so the test is deterministic and repeatable
    await vector_db_service.reset()

    count_before = await vector_db_service.count()
    print("Vector DB count before ingestion:", count_before)
    assert count_before == 0, "Expected an empty collection after reset"

    result = await ingestion_service.ingest_pdf(
        "data/papers/2201.00978v1.pdf",
        {
            "document_id": "pyramid_tnt",
            "title": "PyramidTNT: Revisiting Hierarchical Vision Transformer",
            "source": "arxiv",
        },
    )

    print("Ingestion result:", result)
    assert result["chunks"] > 0, "Expected at least one chunk to be generated"
    assert result["status"] == "completed", "Expected ingestion status to be 'completed'"

    count_after = await vector_db_service.count()
    print("Vector DB count after ingestion:", count_after)
    assert count_after > count_before, "Vector DB count did not increase after ingestion"
    assert count_after == result["chunks"], "Stored vector count does not match chunk count"

    print("\nIngestion validation PASSED")
    print("- chunks generated:", result["chunks"])
    print("- embeddings generated and stored:", count_after)


asyncio.run(main())
