from pydantic import BaseModel
from typing import List, Optional


class Article(BaseModel):
    title: str
    description: Optional[str] = None
    url: str
    source: str


class NewsResponse(BaseModel):
    total_results: int
    articles: List[Article]
