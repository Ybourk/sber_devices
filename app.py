from uuid import UUID

from fastapi import FastAPI

from models import Movie, MovieInfo, SearchResponse, MovieInfoResponse
from utils import (mocked_provider_movie_response,
                   mocked_provider_searh_response)

API_V1_PREFIX = '/api/v1'
app = FastAPI(
    title='Sber Devices Test System "B" API',
    openapi_url=f"{API_V1_PREFIX}/openapi.json",
    docs_url=f"{API_V1_PREFIX}/docs"
)


@app.get(f"{API_V1_PREFIX}/search")
async def search_by_name(name: str, systemCode: str) -> SearchResponse:
    provider_api_response = await mocked_provider_searh_response(name, systemCode.upper())

    return SearchResponse(
        messageId=provider_api_response.messageId,
        systemCode=provider_api_response.systemCode,
        created=provider_api_response.created,
        movies=[Movie(**m.dict()) for m in provider_api_response.movies] if provider_api_response.movies else [],
    )


@app.get(f"{API_V1_PREFIX}/movies/show")
async def show(movieId: UUID, systemCode: str) -> MovieInfoResponse:
    provider_api_response = await mocked_provider_movie_response(movieId, systemCode.upper())

    return MovieInfoResponse(
        messageId=provider_api_response.messageId,
        systemCode=provider_api_response.systemCode,
        created=provider_api_response.created,
        movie=MovieInfo(**provider_api_response.movie.dict()),
    )
