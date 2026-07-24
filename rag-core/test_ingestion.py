import asyncio

from app.services.ingestion.ingestion_service import ingestion_service
from app.services.vector_db.vector_db_service import vector_db_service


async def main():

    result = await ingestion_service.ingest_pdf(
        "data/papers/2201.00978v1.pdf",
        {
            "document_id": "pyramid_tnt",
            "source": "arxiv",
        },
    )

    print(
        "Ingestion result:",
        result,
    )

    count = await vector_db_service.count()

    print(
        "Vector DB count:",
        count,
    )


asyncio.run(main())