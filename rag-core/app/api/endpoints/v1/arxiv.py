from fastapi import APIRouter
from app.services.arxiv.arxiv_service import arxiv_service

router = APIRouter()

@router.get(
    "/arxiv/search",
    summary="Search for papers on arXiv"
)
async def search_arxiv(query: str):
    papers = await arxiv_service.search(query)
    return papers