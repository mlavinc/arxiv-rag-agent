from fastapi import APIRouter
from app.services.arxiv.arxiv_service import arxiv_service
from app.services.arxiv.pdf_downloader_service import pdf_downloader_service

router = APIRouter()

@router.get(
    "/arxiv/search",
    summary="Search for papers on arXiv"
)
async def search_arxiv(query: str):
    papers = await arxiv_service.search(query)
    return papers

@router.post(
    "/arxiv/download",
    summary="Download arXiv paper PDF"
)
async def download_pdf(paper_id: str):
    path = await pdf_downloader_service.download(
        paper_id
    )
    return {
        "file": path
    }