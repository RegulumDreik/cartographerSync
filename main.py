from fastapi import FastAPI

from src.interface.rest.api import api_router

app = FastAPI()

app.include_router(api_router)
print('Hello')
print('hello')
print('1231')