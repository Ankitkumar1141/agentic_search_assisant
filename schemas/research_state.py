from typing import Optional

from pydantic import BaseModel, Field


class ResearchState(BaseModel):
    """Shared state passed between agents in the research workflow."""

    topic: str = Field(..., description="Research topic provided by the user")
    search_results: Optional[str] = Field(
        default=None, description="Raw output from the search agent"
    )
    scraped_content: Optional[str] = Field(
        default=None, description="Extracted content from the reader agent"
    )
    report: Optional[str] = Field(
        default=None, description="Final research report from the writer agent"
    )
    feedback: Optional[str] = Field(
        default=None, description="Critic review and score of the report"
    )

    def to_dict(self) -> dict:
        return self.model_dump()
