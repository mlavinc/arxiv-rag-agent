from app.schemas.search import SearchResponse
from app.services.embeddings.embeddings_service import embeddings_service
from app.services.vector_db.vector_db_service import vector_db_service
from app.services.llm.llm_service import llm_service


class RAGService:
    """
    Handles the RAG pipeline orchestration.
    """

    def search(self, question: str) -> SearchResponse:
        # Step 1: Generate embedding
        embedding = embeddings_service.embed(question)

        # Step 2: Search relevant documents
        context = vector_db_service.search(embedding)

        # Step 3: Generate final answer
        answer = llm_service.generate(question, context)

        return SearchResponse(
            answer=answer,
            sources=[]
        )


rag_service = RAGService()