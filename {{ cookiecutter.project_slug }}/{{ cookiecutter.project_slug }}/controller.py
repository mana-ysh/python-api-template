from fastapi import APIRouter, FastAPI
from pydantic import BaseModel


api_v1_router = APIRouter()


class MessageResponse(BaseModel):
    msg: str


@api_v1_router.get("/dummy")
def dummy() -> MessageResponse:
    return MessageResponse(msg="I'm dummy")


def create_app() -> FastAPI:
    app = FastAPI(title="App")

    app.include_router(api_v1_router, prefix="/api/v1")

    @app.get("/health")
    def health() -> MessageResponse:
        return MessageResponse(msg="I'm healthy")

    return app
