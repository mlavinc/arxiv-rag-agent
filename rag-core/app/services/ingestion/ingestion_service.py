from app.services.document.pdf_downloader_service import pdf_downloader_service
from app.services.document.pdf_parser_service import pdf_parser_service
from app.services.document.chunking_service import chunking_service
from app.services.embeddings.embeddings_service import embeddings_service
from app.services.vector_db.vector_db_service import vector_db_service


class IngestionService:
    """
    Orchestrates the document ingestion pipeline.
    """

    async def ingest_pdf(
        self,
        file_path: str,
        metadata: dict,
    ):

        # 1. Extract text
        parsed = pdf_parser_service.extract_text(
            file_path
        )

        # 2. Split into chunks
        chunks = chunking_service.split(
            parsed["text"]
        )

        # 3. Generate embeddings
        embeddings = []

        for chunk in chunks:
            embedding = await embeddings_service.embed(
                chunk
            )
            embeddings.append(embedding)

        # 4. Prepare vector documents
        paper_id = metadata.get("paper_id", "unknown")

        ids = [
            f"{paper_id}_chunk_{i}"
            for i in range(len(chunks))
        ]

        metadatas = [
            {
                **metadata,
                "chunk_index": i,
            }
            for i in range(len(chunks))
        ]

        # 5. Store in vector database
        await vector_db_service.add_documents(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        return {
            "chunks": len(chunks),
            "status": "completed",
        }


ingestion_service = IngestionService()