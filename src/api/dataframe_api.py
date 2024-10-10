from fastapi import APIRouter, HTTPException
from typing import Optional
from src.db.dataframe import (
    get_dataframe_as_dict,
    get_dataframe_info,
    clear_dataframe,
    get_rows,
)
from http import HTTPStatus

db_router = APIRouter(    prefix="/images",
    tags=["images"],
    responses={
        HTTPStatus.CREATED: {"description": "Image created"},
        HTTPStatus.OK: {"description": "Image updated"},
        HTTPStatus.NO_CONTENT: {"description": "Image deleted"},
    },
)


@db_router.get("/df/all", status_code=HTTPStatus.OK)
async def get_all_data():
    data = get_dataframe_as_dict()
    if not data:
        raise HTTPException(status_code=404, detail="No data found")
    return data


@db_router.get("/df/info", status_code=HTTPStatus.OK)
async def get_db_info():
    return get_dataframe_info()


@db_router.post("/df/clear", status_code=HTTPStatus.NO_CONTENT)
async def clear_db():
    clear_dataframe()
    return {"message": "Database cleared"}


@db_router.get("/df/rows")
async def get_db_rows(start: int = 0, end: Optional[int] = None):
    data = get_rows(start, end)
    if not data:
        raise HTTPException(
            status_code=404, detail="No data found in the specified range"
        )
    return data
