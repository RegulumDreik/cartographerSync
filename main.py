from fastapi import FastAPI

from src.interface.rest.api import api_router

app = FastAPI(
    title='Cartographer sync Service',
    redoc_url='/api/redoc',
    docs_url='/api/docs',
    openapi_url='/api/openapi.json',
)

app.include_router(api_router)
