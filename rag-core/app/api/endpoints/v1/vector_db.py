from fastapi import APIRouter
from app.services.vector_db.vector_db_service import vector_db_service

router = APIRouter()


@router.get(
    "/vector-db/count",
    summary="Get document count in vector database"
)
async def get_vector_db_count():
    count = await vector_db_service.count()
    return {"documents": count}
