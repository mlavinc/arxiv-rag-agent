from fastapi import APIRouter

from app.services.ingestion.ingestion_service import ingestion_service


router = APIRouter()


@router.post(
    "/ingestion/pdf",
    summary="Ingest a PDF into vector database"
)
async def ingest_pdf(
    file_path: str,
):

    result = await ingestion_service.ingest_pdf(
        file_path=file_path,
        metadata={
            "source": "arxiv",
            "paper_id": "2201.00978",
            "title": "PyramidTNT: Improved Transformer-in-Transformer Baselines with Pyramid Architecture",
        },
    )

    return result