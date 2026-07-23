import chromadb
from app.core.config import settings

class VectorDBService:
    def __init__(self):
        self.client = chromadb.PersistentClient(
            path=settings.CHROMA_PATH,
        )
        self.collection = self.client.get_or_create_collection(
            name=settings.CHROMA_COLLECTION,
            metadata={"hnsw:space": "cosine"},
        )

    async def add_documents(
        self,
        ids: list[str],
        documents: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict[str, str]],
    ) -> None:
        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

    async def search(self, embedding: list[float], n_results: int = 3) -> list[dict]:
        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=n_results,
        )
        documents = []
        for idx in range(len(results["ids"][0])):
            documents.append(
                {
                    "id": results["ids"][0][idx],
                    "document": results["documents"][0][idx],
                    "metadata": results["metadatas"][0][idx],
                    "score": results["distances"][0][idx],
                }
            )
        return documents

    async def count(self) -> int:
        return self.collection.count()

vector_db_service = VectorDBService()
