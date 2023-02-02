from fastapi import FastAPI
from urls.api import router as urls_router

app = FastAPI()

app.include_router(urls_router, tags=["urls"], prefix="/urls")
