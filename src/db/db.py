from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import text, SQLModel
from typing import AsyncGenerator

from src.config import settings

async_engine = create_async_engine(url=settings.POSTGRES_URL, echo=True)

async def init_db():
    async with async_engine.begin() as conn:
        from src.models.images_model import Image
        await conn.run_sync(SQLModel.metadata.create_all)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async_session = sessionmaker(
        bind=async_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with async_session() as session:
        yield session