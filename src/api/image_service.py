from sqlmodel.ext.asyncio.session import AsyncSession
from src.models.images_model import Image
from src.models.schemas import ImageCreateModel
from sqlmodel import select

class ImageService:
    def __init__(self, session):
        self.session = session

    async def get_all_images(self):
        statement = select(Image).order_by(Image.created_at)

        result = await self.session.exec(statement)
        return result.all()
    
    async def create_image(self, image_data: ImageCreateModel):
        new_image = Image(**image_data.model_dump())

        await self.session.add(new_image)
        await self.session.commit()

        return new_image

        
