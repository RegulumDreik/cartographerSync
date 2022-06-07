from fastapi import APIRouter

from src.interface.rest.endpoints.hello import hello_router

api_router = APIRouter()

api_router.include_router(
    hello_router,
    tags=['hello'],
)
