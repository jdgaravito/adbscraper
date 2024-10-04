from fastapi import APIRouter, HTTPException
from typing import Optional
from src.db.df import (
    get_dataframe_as_dict,
    get_dataframe_info,
    clear_dataframe,
    get_rows,
)

db_router = APIRouter()


@db_router.get("/db/all")
async def get_all_data():
    data = get_dataframe_as_dict()
    if not data:
        raise HTTPException(status_code=404, detail="No data found")
    return data


@db_router.get("/db/info")
async def get_db_info():
    return get_dataframe_info()


@db_router.post("/db/clear")
async def clear_db():
    clear_dataframe()
    return {"message": "Database cleared"}


@db_router.get("/db/rows")
async def get_db_rows(start: int = 0, end: Optional[int] = None):
    data = get_rows(start, end)
    if not data:
        raise HTTPException(
            status_code=404, detail="No data found in the specified range"
        )
    return data
