from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        max_length=1000,
        description="Natural language question about AI/ML papers."
    )


class Source(BaseModel):
    title: str
    paper_id: str
    score: float


class SearchResponse(BaseModel):
    answer: str
    sources: list[Source]