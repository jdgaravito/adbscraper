from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.api.ping import ping_router
from src.api.scrapy_api import scrapy_router
from src.api.db_api import db_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    yield
    print("Shutting down...")


app = FastAPI(
    title="AdobeScrapper",
    description="A simple API to scrape alt-text and then turn it into my own images",
    version="0.0.1",
    lifespan=lifespan,
)

app.include_router(ping_router)
app.include_router(scrapy_router)
app.include_router(db_router)
