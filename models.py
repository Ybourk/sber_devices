from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel


# API
class Movie(BaseModel):
    id: UUID
    name: str
    genre: str
    description: Optional[str]
    rating: Optional[str]


class MovieInfo(Movie):
    link: str


class BaseResponse(BaseModel):
    systemCode: str
    messageId: UUID
    created: str


class SearchResponse(BaseResponse):
    movies: List[Movie]


class MovieInfoResponse(BaseResponse):
    movie: MovieInfo


# Provider API
class MockedSearchResponse(SearchResponse):
    pass


class MockedMovieResponse(MovieInfoResponse):
    pass
