from fastapi import APIRouter

from app.schemas.search import SearchRequest, SearchResponse

router = APIRouter()


@router.post(
    "/search",
    response_model=SearchResponse,
    summary="Search indexed ArXiv papers"
)
def search(request: SearchRequest) -> SearchResponse:
    return SearchResponse(
        answer="Search endpoint is working. RAG pipeline not implemented yet.",
        sources=[]
    )