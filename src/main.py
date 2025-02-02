from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.api.ping import ping_router
from src.api.scrapy_api import scrapy_router
from src.api.dataframe_api import db_router
from src.api.images_api import image_router
from src.db.db import init_db



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    await init_db()
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
app.include_router(image_router)
