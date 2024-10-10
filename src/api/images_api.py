from fastapi import APIRouter, Depends
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import List
from src.db.db import get_session
from http import HTTPStatus
from src.api.image_service import ImageService
from src.models.schemas import ImageCreateModel , ImageResponseModel

image_router = APIRouter(
    prefix="/images",
    tags=["images"],
    responses={
        HTTPStatus.CREATED: {"description": "Image created"},
        HTTPStatus.OK: {"description": "Image updated"},
        HTTPStatus.NO_CONTENT: {"description": "Image deleted"},
    },
)


@image_router.get("/", response_model=List[ImageResponseModel])
async def get_images(session: AsyncSession = Depends(get_session)):
    images = await ImageService(session).get_all_images()
    return images


@image_router.get("/{image_id}", status_code=HTTPStatus.OK)
async def get_image(image_id: str, session: AsyncSession = Depends(get_session)):
    pass


@image_router.post("/", status_code=HTTPStatus.CREATED)
async def create_image(
    image_create_data: ImageCreateModel,
    session: AsyncSession = Depends(get_session)):

    new_image = await ImageService(session).create_image(image_create_data)
    return new_image

@image_router.put("/{image_id}", status_code=HTTPStatus.OK)
async def update_image(image_id: str, session: AsyncSession = Depends(get_session)):
    pass

@image_router.delete("/{image_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_image(image_id: str, session: AsyncSession = Depends(get_session)):
    pass