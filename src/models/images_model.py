from sqlmodel import SQLModel, Field, Column
import sqlalchemy.dialects.postgresql as pg
from uuid import UUID, uuid4
from datetime import datetime

class Image(SQLModel, table=True):
    '''This class will contain the image model.'''
    __tablename__ = "images"
    uid: UUID = Field(sa_column=Column(pg.UUID, primary_key=True, unique=True, default=uuid4))
    adobe_image_url: str = Field(nullable=False)
    alt_text: str = Field(nullable=False)
    title: str = Field(nullable=True)
    created_at: datetime = Field(default=datetime.now)
    updated_at: datetime = Field(default=datetime.now)
    file_name: str = Field(nullable=True)
    prompt: str = Field(nullable=True)
    keywords: str = Field(nullable=True)
    sell_amount: int = Field(nullable=True)


    def __repr__(self):
        return f"Image => {self.alt_text}"