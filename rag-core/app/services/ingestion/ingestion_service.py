from app.services.document.pdf_parser_service import pdf_parser_service
from app.services.document.chunking_service import chunking_service
from app.services.embeddings.embeddings_service import embeddings_service
from app.services.vector_db.vector_db_service import vector_db_service


class IngestionService:
    """
    Orchestrates the document ingestion pipeline.

    Flow:
    PDF
      -> Text extraction
      -> Chunking
      -> Embeddings
      -> Vector database
    """

    async def ingest_pdf(
        self,
        file_path: str,
        metadata: dict,
    ) -> dict:

        # 1. Extract text from document
        parsed = pdf_parser_service.extract_text(
            file_path
        )

        text = parsed["text"]

        # 2. Split document into chunks
        chunks = chunking_service.split(
            text
        )

        embeddings = []

        # 3. Generate embeddings
        for chunk in chunks:

            embedding = await embeddings_service.embed(
                chunk
            )

            embeddings.append(
                embedding
            )

        document_id = metadata.get(
            "document_id",
            "unknown",
        )

        # 4. Prepare Chroma documents
        ids = [
            f"{document_id}_chunk_{index}"
            for index in range(len(chunks))
        ]

        document_title = metadata.get(
            "title",
            metadata.get("filename", document_id)
        )
        metadatas = [
            {
                **metadata,
                "title": document_title,
                "chunk_index": index,
            }
            for index in range(len(chunks))
        ]

        # 5. Store vectors
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