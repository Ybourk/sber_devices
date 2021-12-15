from datetime import datetime
from uuid import uuid4, UUID

from models import Movie, MockedSearchResponse, MockedMovieResponse, MovieInfo

SYSTEM_CODE_MAP = {
    "b": "cinema".upper(),
}


async def mocked_provider_searh_response(name: str, system_code: str) -> MockedSearchResponse:
    return MockedSearchResponse(
        messageId=uuid4(),
        created=str(datetime.now()),
        systemCode=SYSTEM_CODE_MAP.get(system_code.lower(), "cinema".upper()),
        movies=[
            Movie(id=uuid4(), name=name, genre="action"),
            Movie(id=uuid4(), name=f"{name} 2", genre="action"),
            Movie(id=uuid4(), name=f"{name} 3", genre="action"),
        ],
    )


async def mocked_provider_movie_response(movieId: UUID, system_code: str) -> MockedMovieResponse:
    return MockedMovieResponse(
        messageId=uuid4(),
        created=str(datetime.now()),
        systemCode=SYSTEM_CODE_MAP.get(system_code.lower(), "cinema".upper()),
        movie=MovieInfo(id=movieId, name=f"The Matrix", genre="action", link="https://cinema/matrix.html"),
    )
