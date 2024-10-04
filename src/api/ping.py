'''This module will contain the ping route.'''
from fastapi import APIRouter

ping_router = APIRouter()


@ping_router.get("/ping")
async def pong():
    '''This function will return a pong! message.'''
    return {
        "ping": "pong!",
        "message": "pong"
    }