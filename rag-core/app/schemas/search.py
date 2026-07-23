from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        max_length=1000,
        description="Natural language question about AI/ML papers."
    )


class Source(BaseModel):
    document_id: str
    title: str
    chunk_index: int
    score: float


class SearchResponse(BaseModel):
    answer: str
    sources: list[Source]