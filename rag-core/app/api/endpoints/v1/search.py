from fastapi import APIRouter

from app.schemas.search import SearchRequest, SearchResponse
from app.services.rag.rag_service import rag_service

router = APIRouter()


@router.post(
    "/search",
    response_model=SearchResponse,
    summary="Search indexed ArXiv papers"
)
def search(request: SearchRequest) -> SearchResponse:
    return rag_service.search(request.question)