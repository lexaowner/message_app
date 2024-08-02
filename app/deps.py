from app.crud import get_messages, create_message
from fastapi import Depends


async def get_db():
    try:
        yield
    finally:
        pass