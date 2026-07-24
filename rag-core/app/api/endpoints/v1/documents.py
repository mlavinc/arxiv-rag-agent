from fastapi import APIRouter, UploadFile, File
from pathlib import Path
from app.services.ingestion.ingestion_service import ingestion_service

from app.services.document.pdf_parser_service import (
    pdf_parser_service
)
from app.services.document.chunking_service import (
    chunking_service
)


router = APIRouter()


@router.get(
    "/documents/extract",
    summary="Extract text from PDF"
)
async def extract_pdf(file_path: str):

    result = pdf_parser_service.extract_text(
        file_path
    )

    return result
@router.get(
    "/documents/chunks",
    summary="Extract PDF text and split into chunks"
)
async def get_chunks(file_path: str):

    parsed = pdf_parser_service.extract_text(file_path)

    chunks = chunking_service.split(
        parsed["text"]
    )

    return {
        "pages": parsed["pages"],
        "chunks": len(chunks),
        "first_chunk": chunks[0] if chunks else None,
    }
@router.post(
    "/documents/ingest",
    summary="Upload and ingest PDF document"
)
async def ingest_document(
    file: UploadFile = File(...)
):

    upload_dir = Path("data/uploads")

    upload_dir.mkdir(
        exist_ok=True
    )

    file_path = upload_dir / file.filename

    content = await file.read()

    file_path.write_bytes(
        content
    )

    result = await ingestion_service.ingest_pdf(
        str(file_path),
        {
            "document_id": file.filename,
            "title": file.filename,
            "source": "upload",
        },
    )

    return {
        "filename": file.filename,
        **result,
    }