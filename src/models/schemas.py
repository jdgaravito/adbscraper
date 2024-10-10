from src.models.images_model import Image
from pydantic import BaseModel
from sqlmodel import Field


class ImageResponseModel(Image):
    '''This class will contain the image response model.'''
    pass

class ImageCreateModel(BaseModel):
    '''This class will contain the image create model.'''
    adobe_image_url: str = Field(title="Adobe Image URL", nullable=False)
    alt_text: str = Field(title="Alt text of the image",nullable=False)
    title: str = Field(nullable=True)
    file_name: str = Field(nullable=True)
    prompt: str = Field(nullable=True)
    keywords: str = Field(nullable=True)
    sell_amount: int = Field(nullable=True)

    class Config:
        '''This class will contain the config for the image create model.'''
        json_schema_extra = {
            "example": {
                "adobe_image_url": "https://stock.adobe.com/contributor/211423356/Flowal93",
                "alt_text": "Alt text of the image",
                "title": "Title of the image",
                "file_name": "image.png",
                "prompt": "Prompt for the image",
                "keywords": "Keywords for the image",
                "sell_amount": 100,
            }
        }