from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from src.db.db import get_session
from http import HTTPStatus

image_router = APIRouter(
    prefix="/images",
    tags=["images"],
    responses={
        HTTPStatus.CREATED: {"description": "Image created"},
        HTTPStatus.OK: {"description": "Image updated"},
        HTTPStatus.NO_CONTENT: {"description": "Image deleted"},
    },
)


@image_router.get("/images", status_code=HTTPStatus.OK)
async def get_images(session: AsyncSession = Depends(get_session)):
    pass

@image_router.get("/images/{image_id}", status_code=HTTPStatus.OK)
async def get_image(image_id: str, session: AsyncSession = Depends(get_session)):
    pass


@image_router.post("/images", status_code=HTTPStatus.CREATED)
async def create_image(session: AsyncSession = Depends(get_session)):
    pass

@image_router.put("/images/{image_id}", status_code=HTTPStatus.OK)
async def update_image(image_id: str, session: AsyncSession = Depends(get_session)):
    pass

@image_router.delete("/images/{image_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_image(image_id: str, session: AsyncSession = Depends(get_session)):
    pass