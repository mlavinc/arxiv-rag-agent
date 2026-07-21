from app.schemas.search import SearchResponse


class RAGService:
    """
    Handles the RAG pipeline orchestration.

    For now, returns a placeholder response.
    """

    def search(self, question: str) -> SearchResponse:
        return SearchResponse(
            answer="Search endpoint is working. RAG pipeline not implemented yet.",
            sources=[]
        )


rag_service = RAGService()